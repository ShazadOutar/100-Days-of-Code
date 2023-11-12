from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")


class QuizInterface:
    # quiz_brain: QuizBrain sets the expected data type to be of QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # create the window as an attribute of the QuizInterface class
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # create the score label
        self.score_label = Label(text="Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # create the canvas to put the questions on
        self.canvas = Canvas(width=300, height=250, bg="white")
        # the question is centered in the card so half the width and half the height
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # get the images for the buttons
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        # create the buttons for True and False
        self.true_button = Button(image=true_image, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.false_button = Button(image=false_image, highlightthickness=0, borderwidth=0, command=self.false_pressed)

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        # set the first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.reset_canvas_bg()
        if self.quiz.still_has_questions():
            # do these while the quiz still has questions left
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # Use the check_answer function from the quiz brain
        is_right = self.quiz.check_answer("True")
        # pass that result to the give_feedback function
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            # for a correct response, change the canvas background to green then back to white
            self.canvas.config(bg="green")
        else:
            # for incorrect the background goes to red
            self.canvas.config(bg="red")
        # after 1 second, move to the next question
        self.window.after(1000, self.get_next_question)

    def reset_canvas_bg(self):
        self.canvas.config(bg="white")
