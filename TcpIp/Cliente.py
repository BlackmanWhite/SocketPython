import socket

HOST = "10.22.10.63"  # The remote host
PORT = 900             # The same port as used by the server
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect((HOST, PORT))

print("Para Sair use ctrl+x\n")
msg = input()

while msg!= "\x18":
    tcp.send(msg.encode("utf8"))
    #data = tcp.recv(1024)
    msg = input()
tcp.close()

