import socket

# Define qual o endereço do servidor
HOST = 'localhost'
PORT = 32320

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor
s.connect((HOST, PORT))


# Envia uma mensagem para o servidor
# s.sendall(b'Hello, world')
s.sendall(str.encode('Hello, world'))
data = s.recv(1024)

# Fecha a conexão
# print('Recebido', repr(data))
print('Recebido:',data.decode())