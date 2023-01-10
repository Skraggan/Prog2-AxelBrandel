import tkinter as tk
import math
from PIL import Image, ImageTk
import random

# Window dimensions
width, height = int(1920/1.5), int(1080/1.5)

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
        self.defeat = False
        self.frame = tk.Frame(window)
        self.frame.pack()

        # A set with coordinates of all tiles
        self.xys = set()
        for x in range(self.n_cols):
            for y in range(self.n_rows):
                self.xys.add((x, y))
        
        self.neighbours = {}
        for (x, y) in self.xys:
            # iterates over a 3x3 grid of each tile and stores a set of each ones neighbours
            # this excludes the center tile and all tiles outside of the playing field
            self.neighbours[x, y] = set((nx, ny) for nx in [x-1, x, x+1] for ny in [y-1, y, y+1]
                                        if (nx, ny) != (x, y) and (nx, ny) in self.xys)

        # resizes the images to fit the tiles in the frame
        def loadImage(img):
            image = Image.open(r"tkinter/minesweeper/" + str(img))
            image = image.resize((self.tile_size,self.tile_size), 2)    
            return ImageTk.PhotoImage(image)

        # for restarting
        def reboot():
            self.frame.destroy()
            restart()

        # loads all of the different images
        self.images = {}
        for i in range(1,9):
            self.images[f"tile_{i}"] = loadImage(f"tile_{i}.gif")
        for name in ["clicked", "flag", "mine", "plain", "wrong"]:
            self.images[f"tile_{name}"] = loadImage(f"tile_{name}.gif")

        # Creates the top bar with information and restart button
        self.text = tk.Label(self.frame, text=f"Bombs remaining: unknown", font=("Times new roman", 18))
        self.button = tk.Button(self.frame, text="Restart?", command=reboot, borderwidth="3", font="bold")
        self.button.grid(column=self.n_cols - self.n_cols//4, row=0, columnspan=self.n_cols//2, sticky="news")
        self.text.grid(column=0, columnspan=self.n_cols - self.n_cols//4, row=0)
        self.frame.columnconfigure(tuple(range(60)), weight=1)
        self.frame.rowconfigure(tuple(range(30)), weight=1)

        self.setup()

    # Adds a bomb wherever possible
    def addBomb(self, exception):
        x = random.randint(0, self.n_cols-1)
        y = random.randint(0, self.n_rows-1)
        if (x, y) in self.bombs or (x,y) == exception:
            return self.addBomb(exception)
        else:
            self.bombs.add((x, y))
            return (x, y)

    # Creates all of the tiles as buttons and also listeners for right and left mousebutton.
    def setup(self):
        self.tiles = {}
        for xy in self.xys:

            self.tiles[xy] = tile = tk.Button(self.frame, image=self.images["tile_plain"])
            tile.grid(row=xy[1]+1, column=xy[0])
        

            def clicked(xy=xy):
                if not self.defeat:
                    self.open(xy)
            tile.config(command=clicked)

            def right_clicked(event, xy=xy):
                if not self.defeat:
                    if xy not in self.flagged:
                        self.flagged.add(xy)
                        print(str(xy) + "flag added")
                    else:
                        self.flagged.remove(xy)
                        print(str(xy) + "flag removed")  
                    self.refresh(xy)
            tile.bind("<Button-3>", right_clicked)

    # Runs on tile xy when clicked. It then calculates which number or bomb it will show. Also if it should autoopen another tile.
    def open(self, xy):
        print(xy)

        if len(self.opened) == 0:
            for i in range(self.n_bombs):
                self.addBomb(xy)

        if xy in self.opened:
            return
        self.opened.add(xy)
        
        if xy in self.bombs:
            self.bombs_near[xy] = "wrong"
            self.lose()
        else:
            self.bombs_near[xy] = len(self.neighbours[xy] & self.bombs)
        
        for neighbour in self.neighbours[xy]:
            if len(self.neighbours[neighbour] & self.bombs) == 0 or self.bombs_near[xy] == 0:
                self.auto_open(neighbour)
        print(len(self.bombs), self.bombs)
        self.refresh(xy)

    # Auto opens sqaures that are empty with recursion
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

    # Refreshes xy tile to show the correct image.
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
        self.text.config(text=f"Bombs remaining: {int(len(self.bombs) - len(self.flagged))}")

    # Un-hides all of the bombs and prevents further clicking
    def lose(self):
        self.defeat = True
        for xy in self.xys:
            if xy in self.bombs:
                self.tiles[xy].config(image=self.images["tile_mine"])

def restart():
    minesweeper = Minesweeper(window, cols, rows, b_density)

# here you can choose columns, rows and density of the bombs
cols = 15
rows = 15
b_density = 0.2

window = tk.Tk()
window.title("Minesweeper")
minesweeper = Minesweeper(window, cols, rows, b_density)
window.mainloop()

