import socket

# Define qual o endereço do servidor
HOST = 'localhost'
PORT = 50001

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# Define o limite de conexões
s.listen()
print("Aguardando conexão de um cliente")

# Aceita uma conexão
conn, ender = s.accept()
print("Conectado em", ender)

# Envia uma mensagem para o cliente
while True:
    data = conn.recv(1024)
    if not data:
        print("Fechando a conexão")
        conn.close()
        break
    print("Recebi:", data)
    conn.sendall(data)