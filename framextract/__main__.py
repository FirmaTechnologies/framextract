'''
usage: framextract <inputfile> --get-info-only -o <outputfolder> -f <framerate>
'''
import cv2
from argparse import ArgumentParser
from pathlib import Path

def get_frame(vidcap, frame_rate, count, frame_folder):
    if frame_rate:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, count*frame_rate*1000)
    hasFrames, frame = vidcap.read()
    if hasFrames:
        cv2.imwrite((frame_folder/f'frame{str(count)}.jpg').as_posix(),
                    frame, [cv2.IMWRITE_JPEG_QUALITY, 100]) # highest quality
    return hasFrames

def main():
    parser = ArgumentParser(description='Extract frames from a video')
    parser.add_argument('--version', action='version', version='%(prog)s 0.2.3')
    parser.add_argument('input', help='input video')
    parser.add_argument('--get-info-only', dest='getinfo', action='store_true',
                        help='print video frame rate and frame size')
    parser.add_argument('--output', '-o', help='output folder')
    parser.add_argument('--framerate', '-f', type=float,
                        help='frame rate that is larger than the original')
    args = parser.parse_args()

    video_name = Path(args.input)
    get_info = args.getinfo
    frame_folder = Path(args.output if args.output else video_name.stem)

    vidcap = cv2.VideoCapture(video_name.as_posix())
    try:
        frame_rate_ori = 1/int(vidcap.get(cv2.CAP_PROP_FPS))
    except ZeroDivisionError as e:
        print(f'Couldn\'t read video stream from file "{video_name}"')
        return e
    frame_rate = args.framerate if (args.framerate and
                                    args.framerate>frame_rate_ori) else None

    if get_info:
        print(f'{video_name.name}:')
        print(f'Frame rate: {frame_rate_ori:.3} s')
        print(f'Frame size: {int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))}',
              f'X {int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))}')
        return

    frame_folder.mkdir(exist_ok=True)

    count = 0
    success = get_frame(vidcap, frame_rate, count, frame_folder)
    while success:
        count += 1
        success = get_frame(vidcap, frame_rate, count, frame_folder)
        if not count%50:
            print(count)
        else:
            print('.', end='')
    print()
    print(f'{count} frames were extracted to "{frame_folder}"')

if __name__ == '__main__':
    main()
