import os
from moviepy import *
os.environ["FFPLAY_BINARY"] = r"C:\Users\FAWWAZ\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffplay.exe"

myclip = VideoFileClip("example.mp4")
myclip = myclip.with_end(5)  # stop the clip after 5 sec
myclip = myclip.without_audio()  # remove the audio of the clip
twb = ImageClip("twb2.png",transparent=True, fromalpha=False, duration=5).resized(0.15).with_position("center")
final = CompositeVideoClip([myclip, twb])
final.preview()
