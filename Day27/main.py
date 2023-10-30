import tkinter


def print_user_input():
    # get the input text and then print it
    user_input = input_field.get()
    print(user_input)


def update_my_label():
    user_input = input_field.get()
    my_label.config(text=user_input)


window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=800, height=600)
# to add padding to the screen, use the same parameters to add padding to individual components
window.config(padx=20, pady=20)

# Create a label
my_label = tkinter.Label(text="Label 1", font=("Ariel", 24))
# my_label.pack(side="left")
# my_label.pack(expand=True)
my_label.config(text="New Text")
# my_label.pack()
my_label.grid(column=0, row=0)


# Create a button
def button_clicked():
    print("Pressed!")
    my_label.config(text="Button Pressed!")


# Use the command as an event listener like in turtle
my_button = tkinter.Button(text="Press me", command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)

# Entry component
input_field = tkinter.Entry()
input_field.config(width=20)
# input_field.pack()
input_field.grid(column=3, row=3)

# user_input = input_field.get()


# print(user_input)


# get_user_input_button = tkinter.Button(text="Submit entry", command=print_user_input)
get_user_input_button = tkinter.Button(text="Submit entry", command=update_my_label)
# get_user_input_button.pack()
get_user_input_button.grid(column=2, row=0)

window.mainloop()
