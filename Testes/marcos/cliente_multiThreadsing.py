import socket
ip = 'localhost'
port = 32323
nome = input("Qual seu nome?\n")
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
print("conectado ao servidor...")
client_socket.send(nome.encode())

while(True):
    #try:
    mensagem = input('Digite: ')
    client_socket.send(mensagem.encode())
    print("Mensagem enviada")
    if mensagem == 'bye':
        client_socket.close()
        break

    #     print('Conexão com o servidor desconectada...')
    #     client_socket.close()
    #     break
    # print('mensagem enviada...')
        #print('mensagem recebida: ' + client_socket.recv(1024).decode())
    #except:
        #client_socket.close()
        #break