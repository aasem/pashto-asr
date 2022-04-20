from __future__ import unicode_literals
from sys import argv


def ytmp3(*args):
    import youtube_dl
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'mp3',
             'preferredquality': '192',
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([argv[1]])

ytmp3(argv[1])