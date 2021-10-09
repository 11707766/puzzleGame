from tkinter import *
from random import *
from tkinter import messagebox
import time
import os
import sys


FOODITEMS_WORD = ['ICER', 'ADL', 'DWANSCHI', 'ZAZIP', 'EABRD', 'NREAPE', 'BSARAM', 'YABIRNI', 'RPIU', 'ITHCAAP', 'RAPAOAT','NATROODI', 'CIPELK',
                  'DAVA', 'MAPU', 'LABGUMUNJA', 'REGUBR','MOUMHSRO', 'DURC']

FOODITEMS_ANSWER = ['RICE', 'DAL', 'SANDWICH', 'PIZZA', 'BREAD', 'PANEER', 'SAMBAR', 'BIRYANI', 'PURI', 'CHAPATI','PAROTA', 'TANDOORI', 'PICKLE',
                    'VADA', 'UPMA', 'GULABJAMUN', 'BURGER', 'MUSHROOM', 'CURD']

ran_num = randrange(0, (len(FOODITEMS_WORD)))
jumbled_rand_word = FOODITEMS_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        import main_start
        main_start.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(FOODITEMS_WORD)))
        word.configure(text=FOODITEMS_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == FOODITEMS_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(FOODITEMS_WORD)))
            word.configure(text=FOODITEMS_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=FOODITEMS_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Quizee-Fooditems_jumbled_words")
    my_window.configure(background="#e6fff5")
    my_window.iconbitmap(os.path.join(sys.path[0], 'quiz_logo.ico'))
    img1 = PhotoImage(file="4_Impementation\Goback.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  30 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10,20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()