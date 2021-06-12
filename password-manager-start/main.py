from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager Program")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
my_image = PhotoImage("logo.png")
canvas.create_image(200,200, image=my_image)
canvas.pack()

window.mainloop()
