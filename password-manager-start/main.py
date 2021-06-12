from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(letters) for _ in range(nr_symbols)]
    password_numbers = [random.choice(letters) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SEARCH -------------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as password_file:
            password_data = json.load(password_file)
            if website in password_data:
                messagebox.showinfo(title=website, message=f"username: {password_data[website]['email']}\npassword: {password_data[website]['password']}")
            else:
                messagebox.showinfo(title="Oops", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if(len(website)==0 or len(username)==0 or len(password)==0):
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #Read old data
                data = json.load(data_file)
                #Update old data with new data
                data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Save the updated data
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Save the updated data
                json.dump(new_data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "best@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Buttons
search_btn = Button(text="Search", command=search, width=13)
search_btn.grid(column=2, row=1)
generate_pass_btn = Button(text="Generate Password", command=generate_password)
generate_pass_btn.grid(column=2, row=3)
add_btn = Button(width=36, text="Add", command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)





window.mainloop()
