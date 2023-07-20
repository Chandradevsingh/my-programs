from moviepy.editor import *

video = VideoFileClip('').subclip(00, 5).rotate(180)
video.write_gif('test.gif')

