import tkinter


def convert_miles_to_km(miles):
    return miles * 1.609


# create a new window
window = tkinter.Tk()
window.title("Miles to Km Converter")
# window.minsize(width=200, height=50)
window.config(padx=20, pady=20)

# create the miles input area
# create the miles input entry
miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=0)


def calculate_and_update():
    # get the miles input, convert to km, and then update the km label
    try:
        x = float(miles_entry.get())
        kms = convert_miles_to_km(x)
        Km_label.config(text=kms)
    except ValueError:
        print("Enter a number")


# create the miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equal to section
text_label = tkinter.Label(text="is equal to")
text_label.grid(column=0, row=1)

# Km result section
# km_value = convert_miles_to_km(get_miles_input())
km_value = 0
# Km display label
Km_label = tkinter.Label(text=f"{km_value}")
Km_label.grid(column=1, row=1)

# Km text label
Km_text_label = tkinter.Label(text="Km")
Km_text_label.grid(column=2, row=1)

# Calculate button
calculate_button = tkinter.Button(text="Calculate", command=calculate_and_update)
calculate_button.grid(column=1, row=2)

window.mainloop()
