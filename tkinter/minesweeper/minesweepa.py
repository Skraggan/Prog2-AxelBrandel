import tkinter as tk
import math
from PIL import Image, ImageTk

width, height = int(1920/2), int(1080/2)

class Minesweeper():

    def __init__(self, window, columns, rows):

        self.n_rows = rows
        self.n_cols = columns
        self.tile_size = int((height-24)/self.n_rows)

        self.frame = tk.Frame(window)
        self.frame.pack()

        self.tiles = set()
        for x in range(self.n_cols):
            for y in range(self.n_rows):
                self.tiles.add((x, y))
        
        self.neighbours = {}
        for (x, y) in self.tiles:
            for nx in [x-1, x, x+1]:
                for ny in [y-1, y, y+1]:
                    if (nx, ny) != (x, y) and (nx, ny) in self.tiles:
                        self.neighbours

        image = Image.open(r"tkinter/minesweeper/tile_plain.gif")
        image = image.resize((self.tile_size,self.tile_size), 2)    
        im = ImageTk.PhotoImage(image)

        text = tk.Label(frame, text="Yuuuuh", font=("Times new roman", 18))
        text.grid(column=0, columnspan=n_cols, row=0)



    def setup():
        tiles = dict()
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
                }
                tile["button"].grid(column=c, row=r+1)
                tiles[r][c] = tile

def main():
    window = tk.Tk()
    minesweeper = Minesweeper(window, 5, 5)
    window.mainloop()

main()
