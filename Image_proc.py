from PIL import Image as i , ImageOps

image = i.open('img2.jpg')
twiboon = i.open('twb4.png')

a, b = twiboon.size

size = ((a,b))

rgba = twiboon.convert("RGBA")
datas = rgba.getdata()
newData = []

r, g, b = 0,0,0

print("image crop style")
print("1. fit")
print("2. pad")
c_style = int(input("enter image crop style "))

print("color cutout")
print("1. Transparant")
print("2. red")
print("3. green")
print("4. blue")
cutout = int(input("color "))


# r,g,b = data from color picker
if cutout == 1:
   pass
elif cutout == 2:
   r = 255
elif cutout == 3:
   g = 255
elif cutout == 3:
   b = 255
def img_process():
   for color in datas:
   # next update make color picker pick exact amout of color so more precise, and maybe try a peformance update using cpp to make the loading faster or just use loading screen in ui
      if color[0] == r and color[1] == g and color[2] == b: # this the change of output of color item
         newData.append((0, 0, 0, 0)) # if the pixel item rgb is 0 (0,0,0,1) then it will make the alpha 0 (0,0,0,0)
      else:
         newData.append(color) # if the pixel have color then just put it back in the array 
         
   rgba.putdata(newData)


   if c_style == 1 :
      result = ImageOps.fit(image, (size))
   elif c_style == 2 :
      result = ImageOps.pad(image, (size), color="#0000")

   result.paste(rgba, (0, 0),mask=rgba)

   result.show()
