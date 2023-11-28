import socket
ip = '10.180.41.148'
port = 7017
nome = input("Qual seu nome?\n")
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
print("passou")
client_socket.send(nome.encode())

while(True):
    #try:
    mensagem = input('digite uma mensagem para enviar ao servidor: ')
    client_socket.send(mensagem.encode())
    print("Mensagem enviada")
    if mensagem == 'bye':
        break
client_socket.close()
    #     print('Conexão com o servidor desconectada...')
    #     client_socket.close()
    #     break
    # print('mensagem enviada...')
        #print('mensagem recebida: ' + client_socket.recv(1024).decode())
    #except:
        #client_socket.close()
        #break