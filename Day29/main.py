from tkinter import *
from tkinter import messagebox
# import random
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # password_list = []
    # Replace these loops by using list comprehension instead
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    # instead of this loop we can use join to add the elements of password_list to the password string
    password = "".join(password_list)
    # print(f"Your password is: {password}")
    # put the password on the password entry and add it to the users clipboard
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO #3: Save the entry data into a data.txt file
# Add data when the add button pressed
def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    # is_ok = False

    # check if the website or password field were left empty
    # all_filled = False
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        # ask the user if the input data is correct
        is_ok = messagebox.askokcancel(title=website_input,
                                       message=f"These are the details entered: \nEmail: {email_input}"
                                               f"\nPassword: {password_input}\nIs it ready to save?")
        if is_ok:
            # append the input data to the file with spaces and linebreak
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website_input} | {email_input} | {password_input}\n")
                # data_file.write(website_input)
                # data_file.write(" | ")
                # data_file.write(email_input)
                # data_file.write(" | ")
                # data_file.write(password_input)
                # # data_file.write(" | ")
                # data_file.write("\n")
            # clear the entry fields after writing the inputs
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(0, "@gmail.com")
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
# TODO #1: Create a canvas with the logo centered. Canvas of 200x200 and 20px of screen padding
# Create the screen window
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Create the canvas to put the image on
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
# add the image to the canvas, *args for create_image are the coordinates of the image
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# TODO #2: Create the layout of the program
# Website input section
# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website input field
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
# sets the cursor to be in the website entry at the start of the program
website_entry.focus()

# Email/Username section
# Email label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Email entry
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
# insert the most common email as the starting email
email_entry.insert(0, "@gmail.com")

# Password section
# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password input
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, columnspan=1)

# Generate password button
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(column=2, row=3)

# Add button section
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
