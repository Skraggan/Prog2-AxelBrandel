import socket

class Client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostname(), 1234))

    while True:
        msg = client.recv(1024).decode("utf-8")
        print(msg)

