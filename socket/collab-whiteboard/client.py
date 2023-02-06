import socket
import tkinter as tk

root = tk.Tk()
root.geometry("1050x570-100-70")
root.resizable(False, False)
root.configure(bg="lightgray")
root.title("Collaborative Whiteboard")

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

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", draw_line)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))

root.mainloop()