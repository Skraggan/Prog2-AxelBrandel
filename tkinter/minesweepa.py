import tkinter as tk
import math

window = tk.Tk()
window.title("MINESWEEPA")

width = 600
height = 600
window.geometry(f"{width}x{height}")

n_rows = 20
n_cols = 20

button_width = width/n_cols
button_height = height/n_rows

count = 1
for r in range(n_rows):
    for c in range(n_cols):
        button = tk.Button(window, text=f"{count}", bg="white", width=20, height=math.floor(height/n_rows))
        button.place(x=c*button_width, y=r*button_height, width=button_width, height=button_height)
        count += 1

window.mainloop()