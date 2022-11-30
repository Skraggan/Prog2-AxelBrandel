import tkinter as tk
import math
from PIL import Image

window = tk.Tk()
window.title("MINESWEEPA")
width, height = int(1920/2), int(1080/2)
# window.geometry(f"{width}x{height}")

frame = tk.Frame(window)
frame.pack()

n_rows = 10
n_cols = 10

button_width = width/n_cols
button_height = height/n_rows

image = Image.open(r"tkinter/minesweeper/tile_plain.gif")
print(image.size)
# im = tk.PhotoImage(file="tkinter/minesweeper/tile_plain.gif")

count = 1
for r in range(n_rows):
    for c in range(n_cols):
        button = tk.Button(frame, image=image)
        # button.place(x=c*button_width, y=r*button_height, width=button_width, height=button_height)
        button.grid(column=c, row=r, )
        count += 1

frame.mainloop()