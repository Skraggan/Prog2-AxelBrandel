import tkinter as tk
from client import Client

HEADERSIZE = 5

root = tk.Tk()
root.geometry("1050x570-100-70")
root.resizable(False, False)
root.configure(bg="lightgray")
root.title("Collaborative Whiteboard")
c = Client()

canvas = tk.Canvas(root, width=900, height=500, cursor="hand2")
canvas.place(x=115, y=35)

draw_size = 5
current_x = 0
current_y = 0

def locate_xy(draw):
    global current_x, current_y
    current_x, current_y = draw.x, draw.y
    point_size = abs(draw_size-3)
    circle = canvas.create_oval(current_x-point_size, current_y-point_size, current_x+point_size, current_y+point_size, fill="black")

def draw_line(draw):
    global current_x, current_y
    line = canvas.create_line(current_x, current_y, draw.x, draw.y, width=draw_size, fill="black", capstyle=tk.ROUND, smooth=True)
    current_x, current_y = draw.x, draw.y
    # print(current_x, current_y, draw.x, draw.y)
    msg = f"{current_x},{current_y},{draw.x},{draw.y}"
    msg = f"{len(msg):<5}"+ msg
    c.client.send(msg.encode("utf-8"))

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", draw_line)

root.mainloop()