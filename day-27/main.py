import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Lable
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() #auto center on screen

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry(width=10)
input.pack()











window.mainloop()