import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) #padx = padding on x

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

#Lable
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack() #auto center on screen
# my_label.place(x=50, y=100)
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
button2 = tkinter.Button(text="new_text")
button2.grid(column=2, row=0)

#Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=3)










window.mainloop()