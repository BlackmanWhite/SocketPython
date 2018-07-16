import socket
import sys

HOST = "0.0.0.0"
PORT = 900
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
print("listen....")
while True:
    conexao, cliente = s.accept()
    print ('Connected by', cliente)
    while True:        
        data = conexao.recv(1024)
        if not(data): break
        print(cliente,data)
    print('Finalizando conexao do cliente', cliente)
    conexao.close()
    sys.exit()
        

