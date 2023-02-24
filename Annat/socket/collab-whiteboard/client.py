import socket
import threading

HEADERSIZE = 5

class Client():
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((socket.gethostname(), 1234))
        self.thread = threading.Thread(target=self.handle)
        self.thread.start()

    def handle(self):
        full_msg = ""
        new_msg = True
        while True:
            msg = self.client.recv(128),
            if new_msg:
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg.decode("utf-8")

            if len(full_msg)-HEADERSIZE == msglen:
                print(full_msg[HEADERSIZE:])
                new_msg = True
                full_msg = ""

        print(full_msg)

