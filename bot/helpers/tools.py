import os
from moviepy.editor import VideoFileClip


def video_details(file_path):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    save_file_path = os.path.dirname(file_path)
    video = VideoFileClip(file_path)
    duration = video.duration
    output = f'{save_file_path}/{file_name}.png'
    video.save_frame(output, t=1.0)
    return duration, output
