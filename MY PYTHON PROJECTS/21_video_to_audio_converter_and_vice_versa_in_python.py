import moviepy.editor

from tkinter.filedialog import *

video = askopenfilename()
video_1 = moviepy.editor.VideoFileClip(video)
audio = video_1.audio
audio.write_audiofile('demo.mp3')
print('--converted--')

