import socket
import threading

IP, PORT = socket.gethostname(), 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen()
print(f"Server is up and running on {IP}:{PORT}")

clients = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client, address):
    while True:
        try:
            message = client.recv(2048).decode("utf-8")
            print(f"Client {str(address)} says: {message}")
            broadcast(message)
        except:
            clients.remove(client)
            print(f"Client {address} disconnected!")
            client.close()
            pass

print("Server running...")

while True:
    conn, addr = server.accept()
    print(f"Connection from {str(addr)} had been established!")
    clients.append(conn)
    broadcast(f"Client {addr} connected to the server".encode("utf-8"))
    conn.send("Connected to the server!".encode("utf-8"))
    thread = threading.Thread(target=handle, args=(conn, addr))
    thread.start()