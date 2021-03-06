from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '*', '(', ')', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_input.delete(0, END)
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, f"{password}")
    pyperclip.copy(f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" and password == "":
        messagebox.showinfo(title="Missing details", message="Please fill in all the required fields.")
    elif website == "":
        messagebox.showinfo(title="Missing details", message="Please enter a website.")
    elif password == "":
        messagebox.showinfo(title="Missing details", message="Please enter a password.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}\n"
                                                              f"Is it ok to save?")

        if is_ok:
            with open("password.txt", mode="a") as password_file:
                password_file.write(f"{website} | {email} | {password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=46)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=46)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "worldcole444@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate", width=10, command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=39, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
