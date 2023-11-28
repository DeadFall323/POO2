import socket

def enviar_dados():
    ip = 'localhost'
    port = 32320
    addr = (ip, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)
    print("Conectado ao servidor")

    # Dados do usuário
    email = "emailkawan"
    senha = "123"

    # Envia dados de login
    login = f"{email},{senha}"
    print("Enviando dados:", login)
    client_socket.send(login.encode('utf-8'))

    # Aguarda resposta do servidor
    print("Aguardando resposta do servidor...")
    recebe = client_socket.recv(1024)
    print("Resposta do servidor:", recebe.decode('utf-8'))


if __name__ == "__main__":
    enviar_dados()
