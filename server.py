import socket
import threading

HEADER = 64
port = 5051
server = socket.gethostbyname(socket.gethostname())
ADDR = (server, port)
FORMAT = 'utf-8'
Disconnect_msg = "DISCONNECTED!"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New connection] {addr} connected.")
    connected = True
    while connected:
        msg_length= conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == Disconnect_msg:
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()
def start():
    s.listen()
    print(f"[LISTENING] Server is listening on {server}")
    while True :

       conn,addr = s.accept()
       thread = threading.Thread(target=handle_client, args=(conn, addr))
       thread.start()
       print(f"[Active connections] {threading.activeCount() - 1}")

start()