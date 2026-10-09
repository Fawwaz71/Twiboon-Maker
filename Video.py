from os import environ
from moviepy import *
from PIL import Image
from screeninfo import get_monitors


environ["FFPLAY_BINARY"] = r"C:\Users\FAWWAZ\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffplay.exe"

twib = 'twb4.png'
video = "example.mp4"


view_size = 0.0
time = 5

monitors = get_monitors()
for monitor in monitors:
    w = monitor.width
    h = monitor.height

#for preview
twiboon = Image.open(twib)
a, b = twiboon.size
print(a,b)

if a < (w-500) and b < (w-500):
  view_size = 0.7
else:
   view_size = 0.15

c = int(a*view_size)
d = int(b*view_size)

print(w,h)

myclip = VideoFileClip(video).with_position("center")
myclip = myclip.with_end(time)  # stop the clip after 5 sec
myclip = myclip.without_audio()  # remove the audio of the clip
twb = ImageClip( twib ,transparent=True, fromalpha=False, duration=time).resized(view_size).with_position("center", relative=True).with_duration(time)
twb.write_videofile("output_video.mp4", fps=24)
gs = VideoFileClip('output_video.mp4')
masked_clip = gs.with_effects([vfx.MaskColor(color=[0, 255, 0], threshold=250, stiffness=100)])


vidtwb = VideoFileClip("twb5.mp4").with_position("center")
e,f = vidtwb.size
if e < (w-500) and f < (w-500):
  view_size = 0.7
else:
   view_size = 0.15
g = int(e*view_size)
h = int(f*view_size)
vid_masked = vidtwb.with_effects([vfx.MaskColor(color=[0, 255, 0], threshold=250, stiffness=100)])

final = CompositeVideoClip([myclip, masked_clip],size=(c,d))
test = CompositeVideoClip([myclip, vid_masked],size=(g,h))
test.preview()

#select the color green or any in color picker and put it on list after that use mask clip for the selected green https://zulko.github.io/moviepy/user_guide/loading.html#mask-clips
# or this https://github.com/Zulko/moviepy/issues/964

#https://www.reddit.com/r/moviepy/comments/c40m78/how_do_i_use_a_green_screen_overlay/ and this for the video