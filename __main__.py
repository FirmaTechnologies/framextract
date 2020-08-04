'''
usage: imgextract <inputfile> -o <outputfolder> -f <framerate>
'''
import cv2, os
from argparse import ArgumentParser
from pathlib import Path

def get_frame(vidcap, frame_rate, count, folder_frame):
    if frame_rate:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, count*frame_rate*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite(f'{folder_frame}{os.path.sep}image{str(count)}.jpg',
                    image, [cv2.IMWRITE_JPEG_QUALITY, 100]) # highest quality
    return hasFrames

def main():
    parser = ArgumentParser(description='Extract frames from a video')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('input', help='input video')
    parser.add_argument('--output', '-o', help='output folder')
    parser.add_argument('--framerate', '-f', type=float, help='frame rate')
    args = parser.parse_args()

    video_name = args.input
    vidcap = cv2.VideoCapture(video_name)
    print(f'Frame size: {int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))}',
          f'{int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))}')
    print(f'Frame rate: {1/int(vidcap.get(cv2.CAP_PROP_FPS))}')

    folder_frame = args.output if args.output else Path(video_name).stem
    frame_rate = args.framerate
    if not os.path.isdir(folder_frame):
        os.makedirs(folder_frame)

    count = 0
    success = get_frame(vidcap, frame_rate, count, folder_frame)
    while success:
        count += 1
        success = get_frame(vidcap, frame_rate, count, folder_frame)
        if not count%100:
            print(count)
        print('.', end='')
    print(f'{count} frames were extracted to {folder_frame}{os.path.sep}')

if __name__ == '__main__':
    main()
