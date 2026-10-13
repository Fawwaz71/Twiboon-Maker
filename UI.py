import customtkinter as ctk
from PIL import Image

def button_callback():
    print("button clicked")
def slider_event(value):
    print(value)

app = ctk.CTk()
app.geometry("600x450")


slider = ctk.CTkSlider(app, from_=0, to=100, command=slider_event)
slider2 = ctk.CTkSlider(app, from_=0, to=100, command=slider_event)
button = ctk.CTkButton(app, text="Pick Color", command=button_callback)
label = ctk.CTkLabel(app, text="Scale", fg_color="transparent")
label2 = ctk.CTkLabel(app, text="Rotation", fg_color="transparent")

button.pack(padx=20, pady=20)
label.pack(padx=0.5, pady=0.5)
slider2.pack(padx=20, pady=20)
label2.pack(padx=0.5, pady=0.5)
slider.pack(padx=20, pady=20)

my_image = ctk.CTkImage(light_image=Image.open('img2.jpg'),
                                  dark_image=Image.open('img2.jpg'),
                                  size=(100, 100))

image_label = ctk.CTkLabel(app, image= my_image, text="")

image_label.pack(padx=40, pady=40)
app.mainloop()

#this is for ctk and tkinter drag and drop and preview
#https://github.com/TomSchimansky/CustomTkinter/discussions/470
#https://www.geeksforgeeks.org/python/browse-upload-display-image-in-tkinter/

#live pillow preview
# still unable to find 