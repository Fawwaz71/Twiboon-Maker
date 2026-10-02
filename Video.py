import os
from moviepy import *
from PIL import Image
os.environ["FFPLAY_BINARY"] = r"C:\Users\FAWWAZ\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffplay.exe"

twib = 'twb2.png'
video = "example.mp4"

#for preview
twiboon = Image.open('twb2.png')
a, b = twiboon.size
a = int(a*0.2)
b = int(b*0.2)

myclip = VideoFileClip(video).with_position("center")
myclip = myclip.with_end(5)  # stop the clip after 5 sec
myclip = myclip.without_audio()  # remove the audio of the clip

twb = ImageClip( twib ,transparent=True, fromalpha=False, duration=5).resized(0.2).with_position("center", relative=True)
final = CompositeVideoClip([myclip, twb],size=(a,b))
final.preview()
