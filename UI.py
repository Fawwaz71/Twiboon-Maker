import customtkinter as ctk

def button_callback():
    print("button clicked")

app = ctk.CTk()
app.geometry("600x450")

button = ctk.CTkButton(app, text="Pick Color", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()