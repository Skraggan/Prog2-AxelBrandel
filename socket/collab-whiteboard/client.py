import socket
import tkinter as tk

root = tk.Tk()
root.geometry("1050x570-100-70")
root.resizable(False, False)
root.configure(bg="lightgray")
root.title("Collaborative Whiteboard")

canvas = tk.Canvas(root, width=900, height=500, cursor="hand2")
canvas.place(x=115, y=35)

current_x = 0
current_y = 0

def locate_xy(draw):
    global current_x, current_y
    current_x, current_y = draw.x, draw.y

def draw_line(draw):
    global current_x, current_y
    line = canvas.create_line(current_x, current_y, draw.x, draw.y, width=2, fill="black")
    current_x, current_y = draw.x, draw.y

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", draw_line)

root.mainloop()