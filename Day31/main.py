from tkinter import *
import pandas
from random import randint
from time import sleep

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
QUESTION_FONT = (FONT_NAME, 40, "italic")
ANSWER_FONT = (FONT_NAME, 60, "bold")
# -------------------------------CREATING FLASHCARDS SECTION-------------------------------
# get the french words from the data file
french_words_data_frame = pandas.read_csv("data/french_words.csv")


# french_words_dictionary = {row.French: row.English for (index, row) in french_words_data_frame.iterrows()}
# print(french_words_dictionary)

# get a column from the data frame
# print(french_words_data_frame.iloc[0])
# get the French and English word from the selected column
# print(french_words_data_frame.iloc[0, 0])
# print(french_words_data_frame.iloc[0, 1])
# to get the number of French words there are in the data frame
# print(french_words_data_frame["French"].size)
# print(french_words_data_frame.iloc[french_words_data_frame["French"].size - 1, 1])

def get_random_word():
    # pick a random number to get the random word from 0 to 1 less than the number of French words
    random_word_index = randint(0, french_words_data_frame["French"].size - 1)
    random_french_word = french_words_data_frame.iloc[random_word_index, 0]
    random_english_word = french_words_data_frame.iloc[random_word_index, 1]
    print(f"fr: {random_french_word}\nen: {random_english_word}")
    return [random_french_word, random_english_word]


# print(get_random_word())

def new_card():
    # show the new card on the front with French
    random_card = get_random_word()
    french_word = random_card[0]
    english_word = random_card[1]
    card.itemconfig(card_question, text="French")
    card.itemconfig(card_answer, text=french_word)

    # show the English side
    card.create_image(450, 300, image=card_back_img)
    # card.itemconfig(card_question, text="English")
    card.create_text(450, 200, text="English", font=QUESTION_FONT, fill="white")
    card.create_text(450, 350, text=english_word, font=ANSWER_FONT, fill="white")


# -------------------------------CARDS SECTION-------------------------------
def show_card():
    # show the new card on the front with French
    random_card = get_random_word()
    french_word = random_card[0]
    english_word = random_card[1]


    card.delete("all")
    show_card_front(french_word)
    window.after(3000)
    show_card_back(english_word)
    # card.


def show_card_front(french_word):
    print(f"Card Front: {french_word}")
    # show the French side
    card.create_image(450, 300, image=card_front_img)
    # card.itemconfig(card_question, text="English")
    card_question = card.create_text(450, 200, text="Question", font=QUESTION_FONT)
    card_answer = card.create_text(450, 350, text="Answer", font=ANSWER_FONT)
    card.grid(column=0, row=0)
    # card.create_text(450, 200, text="French", font=QUESTION_FONT, fill="black")
    # card.create_text(450, 350, text=french_word, font=ANSWER_FONT, fill="black")


def show_card_back(english_word):
    print(f"Card Back: {english_word}")
    # show the English side
    card.create_image(450, 300, image=card_back_img)
    # card.itemconfig(card_question, text="English")
    card.create_text(450, 200, text="English", font=QUESTION_FONT, fill="white")
    card.create_text(450, 350, text=english_word, font=ANSWER_FONT, fill="white")


# -------------------------------UI SECTION-------------------------------
# Create the window
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50)
window.title("Flash Card App")

# Create a canvas for the cards
card = Canvas(width=900, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
# get the images to use
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card.create_image(450, 300, image=card_front_img)
card_question = card.create_text(450, 200, text="Question", font=QUESTION_FONT)
card_answer = card.create_text(450, 350, text="Answer", font=ANSWER_FONT)
card.grid(column=0, row=0, columnspan=2)

# Create the buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=new_card)
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=show_card)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=new_card)
wrong_button.grid(column=1, row=1)

window.mainloop()
