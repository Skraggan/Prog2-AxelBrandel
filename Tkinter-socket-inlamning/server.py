import socket
import threading

class WhiteboardServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(10)
        print(f"Server listening on {self.host}:{self.port}")

    def broadcast_data(self, data, sender):
        for client in self.clients: 
            header = f"{len(data):<10}".encode("utf-8")   
            client.send(header + data)

    def handle_client(self, client):
        self.clients.append(client)
        print(f"New client connected: {client.getpeername()}")
        while True:
            try:
                header = client.recv(10)
                if not header:
                    break
                message_length = int(header.decode("utf-8"))
                data = client.recv(message_length)
                if not data:
                    break
                self.broadcast_data(data, client)
            except ConnectionResetError:
                self.clients.remove(client)
                client.close()

    def run(self):
        while True:
            client, address = self.sock.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client, )).start()

HOST = "localhost"
PORT = 5000

serv = WhiteboardServer(HOST, PORT)
serv.run()