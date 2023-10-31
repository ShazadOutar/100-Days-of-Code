from tkinter import *
from tkinter import messagebox
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#FFCF96"
# RED = "#FF8080"
# GREEN = "#CDFAD5"
# YELLOW = "#F6FDC3"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
# WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# Make timer global so timer reset can access and cancel it
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # noinspection PyTypeChecker
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work Time", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def show_timer_alert():
#     messagebox.showinfo("Timer done", "Continue")
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # When count gets down to 0
        start_timer()
        # window.after(1, show_timer_alert)
        global reps
        marks = ""
        work_sessions = floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create the tomato and time
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Need to use PhotoImage to get the tomato image
tomato_img = PhotoImage(file="tomato.png")
# Create the image at half the width and half the height
# add a bit to the width to avoid the image being cut off
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create the timer label
timer_label = Label(text="Timer")
# fg is the ink color and bg is the background color
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)


# Start button
def start():
    print("start")


start_button = Button(text="Start", command=start_timer, borderwidth=0)
start_button.grid(column=0, row=2)


# Reset button
def reset():
    print("restart")


reset_button = Button(text="Reset", command=reset_timer, borderwidth=0)
reset_button.grid(column=2, row=2)

# checkmarks label
checkmarks = Label()
checkmarks.config(bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

window.mainloop()
