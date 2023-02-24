import tkinter as tk
import socket
import threading

class Whiteboard(tk.Canvas):
    def __init__(self, parent, sock):
        super().__init__(parent)
        self.parent = parent
        self.sock = sock
        self.configure(bg="white")
        self.pack(fill=tk.BOTH, expand=True)

        self.bind("<Button-1>", self.start_paint)
        self.bind("<B1-Motion>", self.draw_paint)
        self.bind("<ButtonRelease-1>", self.end_paint)

        self.start_x, self.start_y = None, None
        self.color = "black"
        self.brush_size = 5

    def send_data(self, data):
        message = str(data).encode("utf-8")
        header = f"{len(message):<10}".encode("utf-8")
        self.sock.send(header + message)

    def start_paint(self, event):
        self.start_x, self.start_y = event.x, event.y

    def draw_paint(self, event):
        if self.start_x and self.start_y:
            x, y = event.x, event.y
            self.create_line(self.start_x, self.start_y, x, y, width=self.brush_size, fill=self.color, capstyle=tk.ROUND, smooth=True)
            self.send_data((False, self.start_x, self.start_y, x, y, self.color, self.brush_size))
            self.start_x, self.start_y = x, y

    def end_paint(self, event):
        self.start_x, self.start_y = None, None

    def set_color(self, color):
        self.color = color

    def set_brush_size(self, size):
        self.brush_size = size

class App(tk.Tk):
    def __init__(self, host, port):
        super().__init__()
        self.title("Whiteboard App")
        self.geometry("800x600")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        print("Connected to the server!")

        self.listen_thread = threading.Thread(target=self.listen_server)
        self.listen_thread.start()

        self.whiteboard = Whiteboard(self, self.sock)

        self.color_var = tk.StringVar(value="Black")
        self.color_menu = tk.OptionMenu(self, self.color_var, "Black", "Red", "Green", "Blue", command=self.change_color)
        self.color_menu.pack(side=tk.LEFT, padx=10, pady=10)

        self.brush_var = tk.IntVar(value=5)
        self.brush_scale = tk.Scale(self, from_=1, to=10, variable=self.brush_var, orient=tk.HORIZONTAL, label="Brush Size", command=self.change_brush_size)
        self.brush_scale.pack(side=tk.LEFT, padx=10, pady=10)

        self.clear_btn = tk.Button(self, text="Clear", command=self.clear_canvas)
        self.clear_btn.pack(side=tk.LEFT, padx=10, pady=10)

    def listen_server(self):
        while True:
            try:
                header = self.sock.recv(10)
                if not header:
                    break
                message_length = int(header.decode("utf-8"))
                data = self.sock.recv(message_length)
                if not data:
                    break
                self.process_data(data.decode("utf-8"))
            except ConnectionResetError:
                break

    def process_data(self, data):
        data_tuple = data[1:-1].split(", ")
        if data_tuple[0] == "False":
            for i in range(len(data_tuple)):
                if i == 5 or i == 0: data_tuple[i] = data_tuple[i][1:-1]
                else: data_tuple[i] = int(data_tuple[i])
            clear_screen, start_x, start_y, x, y, color, brush_size = data_tuple
            self.whiteboard.create_line(start_x, start_y, x, y, width=brush_size, fill=color, capstyle=tk.ROUND, smooth=True)
        else:
            self.whiteboard.delete("all")

    def change_color(self, event=None):
        color = self.color_var.get()
        self.whiteboard.set_color(color)

    def change_brush_size(self, event=None):
        size = self.brush_var.get()
        self.whiteboard.set_brush_size(size)

    def clear_canvas(self):
        self.whiteboard.send_data((True, 0, 0, 0, 0, 0, 0))
        self.whiteboard.delete("all")

HOST = "localhost"
PORT = 5000

app = App(HOST, PORT)
app.mainloop()
