import socket

def iniciar_servidor():
    host = 'localhost'
    port = 32320
    addr = (host, port)

    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen(10)
    print("Servidor iniciado")

    while True:
        print("Aguardando conexão...")
        con, cliente = serv_socket.accept()
        print("Conexão estabelecida")

        # Recebe e imprime os dados do cliente
        dados = con.recv(1024).decode('utf-8')
        print("Dados recebidos:", dados)

        # Fecha a conexão
        con.close()

if __name__ == "__main__":
    iniciar_servidor()
