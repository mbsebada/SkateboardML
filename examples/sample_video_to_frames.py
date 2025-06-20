"""Sample frames from a video in the Tricks directory.
Saves the first few frames as JPEG images.
"""
import cv2
import os
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Tricks')

if len(sys.argv) < 2:
    print('Usage: python sample_video_to_frames.py <relative/path/to/video.mov>')
    sys.exit(1)

video_path = os.path.join(BASE_DIR, sys.argv[1])

if not os.path.exists(video_path):
    sys.exit(f'Video not found: {video_path}')

cap = cv2.VideoCapture(video_path)

frame_id = 0
while frame_id < 5:  # save first 5 frames
    ret, frame = cap.read()
    if not ret:
        break
    out_name = f'frame_{frame_id:03d}.jpg'
    cv2.imwrite(out_name, frame)
    print('Saved', out_name)
    frame_id += 1
cap.release()
