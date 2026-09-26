import cv2 as cv
import numpy as np

def overlay_transparent(bg_img, img_to_overlay_t):
    # Extract the alpha mask of the RGBA image, convert to RGB 
    b,g,r,a = cv.split(img_to_overlay_t)
    overlay_color = cv.merge((b,g,r))

    mask = cv.medianBlur(a,5)

    # Black-out the area behind the logo in our original ROI
    img1_bg = cv.bitwise_and(bg_img.copy(),bg_img.copy(),mask = cv.bitwise_not(mask))

    # Mask out the logo from the logo image.
    img2_fg = cv.bitwise_and(overlay_color,overlay_color,mask = mask)

    # Update the original image with our new ROI
    bg_img = cv.add(img1_bg, img2_fg)

    return bg_img

# def rescale(frame, scale = 0.75):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)

#     dimension = (width,height)

#     return cv.resize(frame, dimension, interpolation= cv.INTER_AREA)


fg_img = "img5.png"
bg_img = "img1.jpg"

bg = cv.imread(bg_img)
fg = cv.imread(fg_img, -1)

a,b = fg.shape[:2]
a = int(a*0.25)
b = int(b*0.25)

bg = cv.resize(bg,(b,a))
fg = cv.resize(fg,(b,a))



# dst = cv.addWeighted(bg,1,fg,0,0.5)

cv.imshow('dst', overlay_transparent(bg,fg))

cv.waitKey(0)
cv.destroyAllWindows()