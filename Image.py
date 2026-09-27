from PIL import Image as i , ImageOps

image = i.open('img2.jpg')
twiboon = i.open('img3.png')

a, b = twiboon.size

size = ((a,b))

rgba = twiboon.convert("RGBA")
datas = rgba.getdata()
newData = []


print("image crop style")
print("1. fit")
print("2. pad")
input = int(input("enter image crop style "))

print(a,b)

for item in datas:

   if item[0] == 0 and item[1] == 0 and item[2] == 0:

       newData.append((255, 255, 255, 0))

   else:

      newData.append(item)
      
rgba.putdata(newData)

if input == 1 :
   result = ImageOps.fit(image, (size))
elif input == 2 :
   result = ImageOps.pad(image, (size), color="#0000")

result.paste(rgba, (0, 0),mask=rgba)

result.show()
