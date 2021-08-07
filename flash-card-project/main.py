BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

current_card = {}
to_learn = {}

try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
    # rand_i = random.randint(0, len(data_file) - 1)
except FileNotFoundError:
    original_data = pandas.read_csv("data/hindi_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")



def gen_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    #rand_h = data_file.loc[rand_i]['Hindi']
    canvas.itemconfig(title, text='Hindi', fill="black")
    canvas.itemconfig(word, text=current_card['Hindi'], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer= window.after(3000, func=flip_card)

def flip_card():
    # rand_e = data_file.loc[rand_i]['English']
    canvas.itemconfig(title, text='English', fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=back_img)

def know_word():
    to_learn.remove(current_card)
    gen_word()
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)






# -------------------UI----------------------------

window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
#card_front = canvas.create_image(400, 263, image=front_img)
card_background = canvas.create_image(400, 263, image=front_img)

title = canvas.create_text(400, 153, text='', fill='black', font=('Ariel', 30, 'italic'))
word = canvas.create_text(400, 263, text='', fill='black', font=('Ariel', 50, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image=PhotoImage(file='images/wrong.png')
unknown_button=Button(image=cross_image, border=0, highlightthickness=0, command=gen_word)
unknown_button.grid(row=1, column=0)

tick_image=PhotoImage(file='images/right.png')
known_button=Button(image=tick_image, border=0, highlightthickness=0, command=know_word)
known_button.grid(row=1, column=1, )


gen_word()

window.mainloop()