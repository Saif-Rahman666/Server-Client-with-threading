import socket

HEADER = 64
PORT = 5051
FORMAT = 'utf-8'
Disconnect_msg = "DISCONNECTED!"
server = socket.gethostbyname(socket.gethostname())
addr = (server,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length =str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("hello")
input()
#send(Disconnect_msg)



