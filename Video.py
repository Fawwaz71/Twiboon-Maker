from os import environ
from moviepy import *
from PIL import Image
from screeninfo import get_monitors

environ["FFPLAY_BINARY"] = r"C:\Users\FAWWAZ\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffplay.exe"

twib = 'twb3.png'
video = "example.mp4"

view_size = 0.2
time = 5

monitors = get_monitors()
for monitor in monitors:
    w = monitor.width
    h = monitor.height

#for preview
twiboon = Image.open(twib)
a, b = twiboon.size
print(a,b)
c = int(a*view_size)
d = int(b*view_size)
print(w,h)

myclip = VideoFileClip(video).with_position("center")
myclip = myclip.with_end(time)  # stop the clip after 5 sec
myclip = myclip.without_audio()  # remove the audio of the clip

twb = ImageClip( twib ,transparent=True, fromalpha=False, duration=time).resized(view_size).with_position("center", relative=True)
final = CompositeVideoClip([myclip, twb],size=(c,d))
final.preview()
