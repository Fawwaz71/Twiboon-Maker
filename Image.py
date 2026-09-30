from PIL import Image as i , ImageOps

image = i.open('img2.jpg')
twiboon = i.open('twb3.png')

a, b = twiboon.size

size = ((a,b))

rgba = twiboon.convert("RGBA")
datas = rgba.getdata()
newData = []


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

print(a,b)

for color in datas:
# next update make color picker pick exact amout of color so more precise, and maybe try a peformance update using cpp to make the loading faster or just use loading screen in ui
   if cutout == 1 and color[0] == 0 and color[1] == 0 and color[2] == 0: # this the change of output of color item
      newData.append((0, 0, 0, 0)) # if the pixel item rgb is 0 (0,0,0,1) then it will make the alpha 0 (0,0,0,0)
   elif cutout == 2 and color[0] >= 0 and color[1] == 0 and color[2] == 0: # to remove red color 
      newData.append((0, 0, 0, 0)) # note for update give to input color using color picker
   elif cutout == 3 and color[0] == 0 and color[1] >= 0 and color[2] == 0: # to remove green color 
      newData.append((0, 0, 0, 0)) # note for update give to input color using color picker
   elif cutout == 4 and color[0] == 0 and color[1] == 0 and color[2] >= 0: # to remove blue color 
      newData.append((0, 0, 0, 0)) # note for update give to input color using color picker
   else:
      newData.append(color) # if the pixel have color then just put it back in the array 
      
rgba.putdata(newData)


if c_style == 1 :
   result = ImageOps.fit(image, (size))
elif c_style == 2 :
   result = ImageOps.pad(image, (size), color="#0000")

result.paste(rgba, (0, 0),mask=rgba)

result.show()
