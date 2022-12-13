import tkinter as tk
import math
from PIL import Image, ImageTk
import random

width, height = int(1920/2), int(1080/2)

class Minesweeper():

    def __init__(self, window, columns, rows, bombs):
        self.n_rows = rows
        self.n_cols = columns
        self.tile_size = int((height-24)/self.n_rows)
        self.n_bombs = bombs
        self.bombs = set()

        self.frame = tk.Frame(window)
        self.frame.pack()

        self.tiles = set()
        for x in range(self.n_cols):
            for y in range(self.n_rows):
                self.tiles.add((x, y))
        
        self.neighbours = {}
        for (x, y) in self.tiles:
            # iterates over a 3x3 grid of each tile and stores a set of each ones neighbours
            self.neighbours[x, y] = set((nx, ny) for nx in [x-1, x, x+1] for ny in [y-1, y, y+1]
                                        if (nx, ny) != (x, y) and (nx, ny) in self.tiles)

        def addBomb():
            x = random.randint(1, self.n_cols)
            y = random.randint(1, self.n_rows)
            if (x, y) in self.bombs:
                return addBomb()
            else:
                self.bombs.add((x, y))
                return (x, y)

        for i in range(self.n_bombs):
            addBomb()

        def loadImage(img):
            image = Image.open(r"tkinter/minesweeper/" + str(img))
            image = image.resize((self.tile_size,self.tile_size), 2)    
            return ImageTk.PhotoImage(image)

        # loads all of the different images
        self.images = {}
        for i in range(1,9):
            self.images[f"tile_{i}"] = loadImage(f"tile_{i}.gif")
        for name in ["clicked", "flag", "mine", "plain", "wrong"]:
            self.images[f"tile_{name}"] = loadImage(f"tile_{name}.gif")

        text = tk.Label(self.frame, text="Yuuuuh", font=("Times new roman", 18))
        text.grid(column=0, columnspan=self.n_cols, row=0)

        self.setup()

    def setup(self):
        for (x, y) in self.tiles:
            tile = tk.Button(self.frame, image=self.images["tile_plain"])
            tile.grid(row=y+1, column=x)

            def clicked(xy=(x, y)):
                # self.open(xy)
                print(xy)
            tile.config(command=clicked)

            def right_clicked(event, xy=(x, y)):
                print(xy)
            tile.bind("<Button-3>", right_clicked)

            

    def open(self, xy):
        print(xy)

def main():
    window = tk.Tk()
    minesweeper = Minesweeper(window, 6, 6, 3)
    window.mainloop()

main()
