import tkinter as tk
import math
from PIL import Image, ImageTk
import random

width, height = int(1920/2), int(1080/2)

class Minesweeper():

    def __init__(self, window, columns, rows, bomb_density):
        self.n_rows = rows
        self.n_cols = columns
        self.tile_size = int((height-24)/self.n_rows)
        self.n_bombs = int(bomb_density*columns*rows)
        self.bombs = set()
        self.bombs_near = {}
        self.opened = set()
        self.flagged = set()

        self.frame = tk.Frame(window)
        self.frame.pack()

        self.xys = set()
        for x in range(self.n_cols):
            for y in range(self.n_rows):
                self.xys.add((x, y))
        
        self.neighbours = {}
        for (x, y) in self.xys:
            # iterates over a 3x3 grid of each tile and stores a set of each ones neighbours
            self.neighbours[x, y] = set((nx, ny) for nx in [x-1, x, x+1] for ny in [y-1, y, y+1]
                                        if (nx, ny) != (x, y) and (nx, ny) in self.xys)

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
        self.tiles = {}
        for xy in self.xys:

            self.tiles[xy] = tile = tk.Button(self.frame, image=self.images["tile_plain"])
            tile.grid(row=xy[1]+1, column=xy[0])
        

            def clicked(xy=xy):
                self.open(xy)
            tile.config(command=clicked)

            def right_clicked(event, xy=xy):
                if xy not in self.flagged:
                    self.flagged.add(xy)
                    print(str(xy) + "flag added")
                else:
                    self.flagged.remove(xy)
                    print(str(xy) + "flag removed")  
                self.refresh(xy)
            tile.bind("<Button-3>", right_clicked)

    def open(self, xy):
        if xy in self.opened:
            return
        self.opened.add(xy)
        
        if xy in self.bombs:
            self.bombs_near[xy] = "mine"
            self.lose()
        else:
            self.bombs_near[xy] = len(self.neighbours[xy] & self.bombs)
        
        for neighbour in self.neighbours[xy]:
            if len(self.neighbours[neighbour] & self.bombs) == 0:
                self.auto_open(neighbour)

        self.refresh(xy)

    def auto_open(self, xy):
        if xy in self.opened or xy in self.bombs:
            return
        else:
            self.opened.add(xy)
            self.bombs_near[xy] = len(self.neighbours[xy] & self.bombs)
            self.refresh(xy)
        if self.bombs_near[xy] == 0:
            for neighbour in self.neighbours[xy]:
                self.auto_open(neighbour)

    def refresh(self, xy):
        tile = self.tiles[xy]
        if xy in self.opened:
            bn = self.bombs_near[xy]
            if bn == 0: bn = "clicked"
            tile.config(image=self.images[f"tile_{bn}"])
        elif xy in self.flagged:
            tile.config(image=self.images["tile_flag"])
        else:
            tile.config(image=self.images["tile_plain"])
        print(self.flagged)
 
    def lose(self):
        for xy in self.xys:
            if xy in self.bombs:
                self.tiles[xy].config(image=self.images["tile_mine"])
    
def main():
    window = tk.Tk()
    minesweeper = Minesweeper(window, 20, 20, 0.3)
    window.mainloop()

main()
