from PIL import Image as i , ImageOps

image = i.open('img1.jpg')
twiboon = i.open('img4.png')

a, b = twiboon.size

rgba = twiboon.convert("RGBA")
datas = rgba.getdata()
newData = []

for item in datas:

   if item[0] == 0 and item[1] == 0 and item[2] == 0:

       newData.append((255, 255, 255, 0))

   else:

      newData.append(item)
      
rgba.putdata(newData)

resize = image.resize((a,b))

resize.paste(rgba, (0, 0),mask=rgba)


resize.show()


print(a,b)