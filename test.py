import cv2
path = "img3.png"

img = cv2.imread(path)
a,b = img.shape[:2]
print(a,b)