from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
# import random
from random import randint, choice, shuffle
import pyperclip
import json


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
    website_input = website_entry.get().title()
    email_input = email_entry.get()
    password_input = password_entry.get()
    # is_ok = False
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
    }

    # check if the website or password field were left empty
    # all_filled = False
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        # ask the user if the input data is correct
        # is_ok = messagebox.askokcancel(title=website_input,
        #                                message=f"These are the details entered: \nEmail: {email_input}"
        #                                        f"\nPassword: {password_input}\nIs it ready to save?")
        is_ok = True
        if is_ok:
            # First try to read the file, if it doesn't exist, then make the file from the new data.
            # If it does exist the json file is updated
            try:
                with open("data.json", mode="r") as data_file:
                    # json.dump is what's used for writing to json files
                    # indent is just for spacing the file, so it's easier to read
                    # json.dump(new_data, data_file, indent=4)

                    # json.load(file_path) reads the json file and returns a python dictionary of it's data

                    # data = json.load(data_file)
                    # print(data)

                    # use data.update to add more data to the json
                    # first load the current json data
                    # data = json.load(data_file)
                    # # update the json data with the new data
                    # data.update(new_data)
                    # json.dump(data, data_file, indent=4)
                    data = json.load(data_file)
            except (FileNotFoundError, JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # write the updated data to the json data file
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.insert(0, "@gmail.com")
                website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
# TODO: Create a find_password function to match the website name
def find_password():
    # check if the input website matches any in the json data
    # first load the json data
    website_input = website_entry.get().title()
    with open("data.json", "r") as file_data:
        data = json.load(file_data)
        # print(data)
        # print(type(data)) # is of type dict
        if website_input in data:
            # If website match found, display the messagebox
            # print(data[website_input])
            email = data[website_input]["email"]
            password = data[website_input]["password"]
            messagebox.showinfo(f"{website_input}", f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Oops", f"No details for the website {website_input} found")
            # print(f"{website_input} not found")

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
website_entry = Entry(width=37)
website_entry.grid(column=1, row=1, columnspan=1)
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

# Search button
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
