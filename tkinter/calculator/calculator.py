import tkinter as tk
from tkinter import font
import tkinter
from tkinter.constants import RIGHT
from typing import Sized
import math

window = tk.Tk()
window.title("The ultimate calculator")
window.geometry("335x515")

global entry_font
entry_font = tkinter.font.Font(size = 22)

global button_font
button_font = tkinter.font.Font(size = 7)

buttons = [
    ["C", "√", "^", "(", ")"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", "=", "/"]
]

exceptions = ["C", "√", "^", "+", "-", "*", "/"]
calc_exceptions = ["C", "√", "^", "%", "="]
symbols_right = ["+", "-", "*", "/" ]

entry = tk.Entry(window, font=entry_font, justify=tk.RIGHT, relief=tk.SUNKEN, bd=15, width=19)

def insertText(event):
    new_text = event.widget.cget("text")
    if new_text == "=":
        calculate()
    elif new_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, new_text)

def calculate():
    result = eval(entry.get().replace("^", "**").replace("√", "sqrt"), {"__builtins__": None, "sqrt": math.sqrt})
    entry.delete(0, tk.END)
    entry.insert(0, result)

for i in range(0, len(buttons)):
    for u in range(0, len(buttons[i])):
        text = buttons[i][u]
        color = "lightgray"
        if text == "=":
            color = "orange"
            button = tk.Button(window, text=text, bg=color, width=10, height=5, relief=tk.RAISED, bd=4)
        elif text == "(" or text == ")":
            color = "gray"
            button = tk.Button(window, text=text, bg=color, width=4, height=5, relief=tk.RAISED, bd=4)
        elif text in exceptions:
            button = tk.Button(window, text=text, bg="gray", width=10, height=5, relief=tk.RAISED, bd=4)
        else:
            button = tk.Button(window, text=text, bg=color, width=10, height=5, relief=tk.RAISED, bd=4)
        if not text in symbols_right:
            button.grid(row=i+1, column=u)
        else:
            button.grid(row=i+1, column=u, columnspan=u+1)

window.bind("<Button-1>", insertText)

entry.grid(row=0, column=0, columnspan=5)

window.mainloop()