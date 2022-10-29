import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

buttonState = "Record"

def record():
    global buttonState
    if buttonState == "Record":
        button['text'] = "Stop"
        buttonState = "Stop"
    else:
        button['text'] = "Record"
        buttonState = "Record"


root = tk.Tk()
root.title("OneVoice")
root.resizable(0, 0)

title = Label(root, text="OneVoice",font='Helvetica 14 bold')
title.grid(row=0,column=0, padx=1, pady=1)

button = Button(root, text=buttonState, width=8, command=record)
button.grid(row=0,column=1, padx=1, pady=1)

canvas = Canvas(root, bg="white", width=600)
canvas.grid(row=1,column=0,  padx=1, pady=1, columnspan=2)

output = Text(root, width=63, height=1)
output.grid(row=2,column=1, columnspan=1,  padx=1, pady=5)

label = Label(root, text="Converted text:")
label.grid(row=2, column=0)

root.mainloop()