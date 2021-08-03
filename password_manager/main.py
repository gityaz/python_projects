from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_symbols + password_letters + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    if len(pass_entry.get()) == 0:
        pass_entry.insert(0, password)
        print(f"Your password is: {password}")
        pyperclip.copy(password)
    else:
        pass_entry.delete(0, END)
        generate_password()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Fields Empty", message="Error: Fields Empty\nPlease enter the values!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You have entered the following details\n Email: {email}\nPassword:{password}\n Do you want to save the details?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                pass_entry.delete(0, END)
                website_entry.focus()
                email_entry.insert(0, "yazisinsirmvit@gmail.com")

def find_password():
    user_entry = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No File", message="No Data file found")
    else:
        #keys_list = data.keys()
        if user_entry in data:
            email = data[user_entry]['email']
            password = data[user_entry]['password']
            messagebox.showinfo(title="Search results", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="No Entry", message=f"No Entry for {user_entry} found")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=100)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "yazisinsirmvit@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Pasword", width=10, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window,mainloop()