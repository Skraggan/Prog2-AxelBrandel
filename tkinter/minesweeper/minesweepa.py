import tkinter as tk
import math
from PIL import Image, ImageTk


window = tk.Tk()
window.title("MINESWEEPA")
width, height = int(1920/2), int(1080/2)
# window.geometry(f"{width}x{height}")

frame = tk.Frame(window)
frame.pack()

n_rows = 5
n_cols = 5

button_size = int((height-24)/n_rows)

image = Image.open(r"tkinter/minesweeper/tile_plain.gif")
image = image.resize((button_size,button_size), 2)
im = ImageTk.PhotoImage(image)

text = tk.Label(frame, text="Yuuuuh", font=("Times new roman", 18))
text.grid(column=0, columnspan=n_cols, row=0)

tiles = dict()
count = 1
for r in range(n_rows):
    for c in range(n_cols):
        if c == 0:
            tiles[r] = {}
        
        tile = {
            "isMine": False,
            "cords": {
                "c": c,
                "r": r
            },
            "button": tk.Button(frame, image=im),
            "mines": 0,
            "id": count
        }
        tile["button"].grid(column=c, row=r+1)
        tiles[r][c] = tile

        count += 1

print(tiles[0][0])

frame.mainloop()