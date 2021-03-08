from tkinter import *
from random import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
card_dict = {}
words_to_learn = {}
try:
    words_remaining_df = pd.read_csv("data/remaining_words_to_learn.csv")
except FileNotFoundError:
    words_original_df = pd.read_csv("data/french_words.csv")
    words_to_learn = words_original_df.to_dict(orient="records")
else:
    words_to_learn = words_remaining_df.to_dict(orient="records")


def next_card():
    global card_dict, flip_timer
    window.after_cancel(flip_timer)
    card_dict = choice(words_to_learn)
    french_word = card_dict["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{french_word}", fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global card_dict
    english_word = card_dict["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{english_word}", fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def known_card():
    words_to_learn.remove(card_dict)
    remaining_words_to_learn = pd.DataFrame(words_to_learn)
    remaining_words_to_learn.to_csv("data/remaining_words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
known_button = Button(image=tick_image, command=known_card)
known_button.grid(row=1, column=2)
next_card()

window.mainloop()
