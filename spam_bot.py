import time
from tkinter import *

import pyautogui

window = Tk()
window.geometry("350x250")
window.title("Spam Bot")

def openwindow():
    new window = Toplevel(root)
    new_window.geometry("350x250")
    new_wi
    lbl = Label(new_window, text="New window")


def spam():
    spam_word = e1.get()
    spam_quantity = e2.get()
    e1.delete(0, END)
    e2.delete(0, END)
    count = 0
    time.sleep(10)
    while count <= (int(spam_quantity)):
        pyautogui.typewrite(spam_word)
        pyautogui.press("enter")
        count += 1


def dev_note():
    notes = Label(window, text="This app is made by Aadhithyan.", font="times 10")
    notes.place(x=0, y=200)


label1 = Label(window, text="SPAM BOT", font="times 14 bold")
label1.place(x=130, y=20)

label2 = Label(window, text="spam word", font="times 12")
label2.place(x=50, y=50)

label4 = Label(window, text="Press the button and put ur cursor wherever u want to spam.", font="times 10")
label4.place(x=0, y=220)

e1 = Entry(window)
e1.place(x=40, y=80)

label3 = Label(window, text="spam quantity", font="times 12")
label3.place(x=210, y=50)

e2 = Entry(window)
e2.place(x=200, y=80)

b1 = Button(window, text='spam!!', width=20, command=spam)
b1.place(x=100, y=140)

b2 = Button(window, text="Dev notes", width=20, command=dev_note)
b2.place(x=100, y=170)

window.mainloop()