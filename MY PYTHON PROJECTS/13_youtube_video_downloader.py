from pytube import YouTube, Playlist

# link = 'https://www.youtube.com/watch?v=EAYlckSaviI&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=12'

# youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)
# # videos = youtube_1.streams        #All Format
# # audios = youtube_1.streams.filter(only_audio=True)        #Audio Format
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# print()
# strm = int(input('Enter : '))
# videos[strm].download()
# print('Video downloaded successfully.')

#Download playlist
Playlist = Playlist('https://www.youtube.com/playlist?list=PLjVLYmrlmjGfoEhXh-ef5QwVCvtWANoTR')
print(f'Downloading...{Playlist.title}')

for video in Playlist.videos:
    video.streams.first().download()

