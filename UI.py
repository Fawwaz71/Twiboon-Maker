import tkinter as tk

window = tk.Tk()
window.title("Twiboon Maker")
window.geometry("720x280")

icon = tk.PhotoImage(file = 'twb1.png')
window.iconphoto(True, icon)
window.config(background="green")

label = tk.Label(window, text="strings", font=("arial", 12,'italic'), bg= 'red')
label.pack()

def handle_button_press():
    window.destroy()

button = tk.Button(text="color picker.", command=handle_button_press)
button.pack()

# Start the event loop
window.mainloop()