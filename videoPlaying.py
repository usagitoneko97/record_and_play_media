"""
# from moviepy.editor import *   ---   be able replace all the import statement below but will cause
                                       pyinstaller to fail to include relevant py file due to some bugs
"""

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import VideoClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.video.io.preview import show, preview

from moviepy.audio.io.preview import preview as audioPreview
import pygame

def play_video(file_name, caption = "shiraishi is best waifu"):
    VideoClip.preview = preview
    VideoClip.show = show

    AudioClip.preview = audioPreview

    pygame.display.set_caption(caption)
    clip = VideoFileClip(file_name)
    clip.preview()
    pygame.quit()


