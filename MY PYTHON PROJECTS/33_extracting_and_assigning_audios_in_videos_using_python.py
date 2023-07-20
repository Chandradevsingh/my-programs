from moviepy.editor import *

# #Audio from Video Extraction
# clip_1 = VideoFileClip('test1.mp4').subclip(0, 20)
# clip_1.audio.write_audiofile('test1.mp3')

# #Video without Audio Creation
# clip_2 = VideoFileClip('test1.mp4').subclip(0, 20)
# clip_2.without_audio()
# clip_2.write_videofile('test_without_audio.mp4')

video_file = VideoFileClip('test_without_audio.mp4')
audio_file = AudioFileClip('test1.mp3')
final_video = video_file.set_audio(audio_file)

