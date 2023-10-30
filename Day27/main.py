import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=800, height=600)

# Create a label
my_label = tkinter.Label(text="Label 1", font=("Ariel", 24))
my_label.pack()
# my_label.pack(side="left")
# my_label.pack(expand=True)
my_label.config(text="New Text")


# Create a button
def button_clicked():
    print("Pressed!")
    my_label.config(text="Button Pressed!")


# Use the command as an event listener like in turtle
my_button = tkinter.Button(text="Press me", command=button_clicked)
my_button.pack()


# Entry component
input_field = tkinter.Entry()
input_field.pack()
input_field.config(width=60)
user_input = input_field.get()
print(user_input)

window.mainloop()
