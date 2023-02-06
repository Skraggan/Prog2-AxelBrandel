import socket
import threading

ip, port = socket.gethostname(), 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(5)
print(f"Server is up and running on {ip}:{port}")

sockets_list = [s]
clients = {}

while True:
    conn, addr = s.accept()
    print(f"Connection from {addr} had been established!")
    conn.send(bytes("You have been connected!", "utf-8"))