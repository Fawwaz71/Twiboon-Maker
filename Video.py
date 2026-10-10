from os import environ
from moviepy import *
from PIL import Image
from screeninfo import get_monitors

environ["FFPLAY_BINARY"] = r"C:\Users\FAWWAZ\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffplay.exe"

view_size = 0.0
time = 5
video = "example.mp4"
vidtwb = VideoFileClip("twb5.mp4").with_position("center")
twib = 'twb4.png'

monitors = get_monitors()
for monitor in monitors:
    w = monitor.width
    h = monitor.height

print("pick if twiboon image or video")
print("1. image")
print("2. Video")
c_style = int(input("twiboon file "))

if c_style == 1:
  twiboon = Image.open(twib)
  a, b = twiboon.size
  if a < (w-500) and b < (w-500):
    view_size = 0.7
  else:
    view_size = 0.15
  width_view = int(a*view_size)
  height_view = int(b*view_size)
else:
  a,b = vidtwb.size
  if a < (w-500) and b < (w-500):
    view_size = 0.8
  else:
    view_size = 0.4
  width_view = int(a*view_size)
  height_view = int(b*view_size)

myclip = VideoFileClip(video).with_position((500,0)).resized(0.5) # make this can be controled
myclip = myclip.with_end(time)  # stop the clip after 5 sec

def imgtwb():
  twb = ImageClip( twib ,transparent=True, fromalpha=False, duration=time).resized(view_size).with_position("center", relative=True).with_duration(time)
  twb.write_videofile("output_video.mp4", fps=24)
  gs = VideoFileClip('output_video.mp4')
  masked_clip = gs.with_effects([vfx.MaskColor(color=[0, 255, 0], threshold=250, stiffness=100)])
  return masked_clip

def videotwb():
  vid_masked = vidtwb.with_effects([vfx.MaskColor(color=[0, 255, 0], threshold=250, stiffness=100)])
  return vid_masked

def preview():
  if c_style == 1:
    final = CompositeVideoClip([myclip, imgtwb()],size=(width_view,height_view))
    final.preview()
  else:
    test = CompositeVideoClip([myclip, videotwb()])
    test.resized(0.7).preview()

def main():
  preview()

main()
#select the color green or any in color picker and put it on list after that use mask clip for the selected green https://zulko.github.io/moviepy/user_guide/loading.html#mask-clips
# or this https://github.com/Zulko/moviepy/issues/964

#https://www.reddit.com/r/moviepy/comments/c40m78/how_do_i_use_a_green_screen_overlay/ and this for the video

#next fix is to fix video scaling since its croping and not scaling down well probabliy cuz the size of the scaling 0.7 and 0.15 is not compatible
# so turn out why the video cropped is because the background video size is smaller than the image thus itcroped the circle, maybe i need to add 3 layer of in video first is the background with the size of twiboon the second is the video i want to put so i can scale whatever i want and last is the twiboon it self
# in preview using the size in compositevideoclip crop the video while resize dont and just put each other on top so most likely use size 