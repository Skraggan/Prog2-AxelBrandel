import socket
import threading
import tkinter as tk

class TicTacToe():
    def __init__(self, window) -> None:

        self.frame = tk.Frame(window, width=480, height=480)
        self.frame.pack()
        for i in range(9):
            button = tk.Button(self.frame, width=20, height=10, command=lambda: self.mark(i//3, i%3))
            button.grid(row=i//3, column=i%3)

        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.winner = None
        self.game_over = False

        self.counter = 0

def host_game(self, host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    client, addr = server.accept()
    threading.Thread(target=self.connection, args=(client,)).start()
    server.close()

def connect_game(self, host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    self.you = "O"
    self.opponent = "X"
    threading.Thread(target=self.connection, args=(client,)).start()



window = tk.Tk()
game = TicTacToe(window)
tk.mainloop()