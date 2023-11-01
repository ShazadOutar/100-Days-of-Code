from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO #3: Save the entry data into a data.txt file
# Add data when the add button pressed
def add_entries():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    with open("data.txt", mode="a") as data_file:
        data_file.write(website_input)
        data_file.write(" | ")
        data_file.write(email_input)
        data_file.write(" | ")
        data_file.write(password_input)
        # data_file.write(" | ")
        data_file.write("\n")

# ---------------------------- UI SETUP ------------------------------- #
# TODO #1: Create a canvas with the logo centered. Canvas of 200x200 and 20px of screen padding
# Create the screen window
window = Tk()
window.title("Password Generator")
# window.config(padx=20, pady=20, height=500, width=500)
window.config(padx=50, pady=50)

# Create the canvas to put the image on
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
# add the image to the canvas, *args for create_image are the coords of the image
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
password_generate_button = Button(text="Generate Password")
password_generate_button.grid(column=2, row=3)

# Add button section
add_button = Button(text="Add", width=35, command=add_entries)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
