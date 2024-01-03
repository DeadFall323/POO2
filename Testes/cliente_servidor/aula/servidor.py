import socket

host = 'localhost'
port = 50021
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)
print("Aguardando conexão")
con, cliente = serv_socket.accept()
print("Conectado")
print("Aguardando mensagem")

while True:
    try:
        recebe = con.recv(1024)
        print("Mensagem recebida: ", recebe.decode('utf-8'))
        if recebe.decode('utf-8') == 'sair':
            print("Conexão encerrada")
            serv_socket.close()
            serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serv_socket.bind(addr)
            serv_socket.listen(10)
            print("Aguardando conexão")
            con, cliente = serv_socket.accept()
            print("Conectado")
            print("Aguardando mensagem")
        else:
            enviar = input("Digite uma mensagem para enviar: ")
            con.send(enviar.encode('utf-8'))
    except Exception as erro:
        serv_socket.close()
        print(str(erro))
