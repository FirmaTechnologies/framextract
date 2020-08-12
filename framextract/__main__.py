'''
usage: framextract <inputfile> --get-info-only -o <outputfolder> -f <framerate>
'''
import cv2, os
from argparse import ArgumentParser
from pathlib import Path

def get_frame(vidcap, frame_rate, count, frame_folder):
    if frame_rate:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, count*frame_rate*1000)
    hasFrames, frame = vidcap.read()
    if hasFrames:
        cv2.imwrite(f'{frame_folder}{os.path.sep}frame{str(count)}.jpg',
                    frame, [cv2.IMWRITE_JPEG_QUALITY, 100]) # highest quality
    return hasFrames

def main():
    parser = ArgumentParser(description='Extract frames from a video')
    parser.add_argument('--version', action='version', version='%(prog)s 0.2.1')
    parser.add_argument('input', help='input video')
    parser.add_argument('--get-info-only', dest='getinfo', action='store_true',
                        help='print video frame rate and frame size')
    parser.add_argument('--output', '-o', help='output folder')
    parser.add_argument('--framerate', '-f', type=float,
                        help='frame rate that is larger than the original')
    args = parser.parse_args()

    video_name = args.input
    get_info = args.getinfo
    frame_folder = args.output if args.output else Path(video_name).stem

    vidcap = cv2.VideoCapture(video_name)
    frame_rate_ori = 1/int(vidcap.get(cv2.CAP_PROP_FPS))
    frame_rate = args.framerate if (args.framerate and
                                    args.framerate>frame_rate_ori) else None

    if get_info:
        print(f'{video_name}:')
        print(f'Frame rate: {frame_rate_ori:.3}')
        print(f'Frame size: {int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))}',
              f'X {int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))}')
        return

    if not os.path.isdir(frame_folder):
        os.makedirs(frame_folder)

    count = 0
    success = get_frame(vidcap, frame_rate, count, frame_folder)
    while success:
        count += 1
        success = get_frame(vidcap, frame_rate, count, frame_folder)
        if not count%100:
            print(count)
        print('.', end='')
    print()
    print(f'{count} frames were extracted to {frame_folder}{os.path.sep}')

if __name__ == '__main__':
    main()
