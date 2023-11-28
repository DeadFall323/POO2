import socket

ip = 'localhost'
port = 32320
addr = (ip, port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(addr)
    print("Conectado")

    while True:
        try:
            email = "ttt"
            senha = "123"

            # Envia dados de login
            login = email + "," + senha
            client_socket.send(login.encode('utf-8'))
            print("Dados de login enviados")

            # Recebe resposta do servidor
            recebe = client_socket.recv(1024)

            if recebe.decode('utf-8') == '1':
                print("Login encontrado")
                # Envia mensagem 'sair' para o servidor

                encerrar = "sair"
                client_socket.send(encerrar.encode('utf-8'))
                # Fecha a conexão após enviar 'sair'
                client_socket.close()
                break

            elif recebe.decode('utf-8') == '0':
                print("Usuario ou senha incorretos")
                client_socket.close()
                break

            else:
                print("Erro ao contactar servidor")
                client_socket.close()
                break

        except Exception as erro:
            print("Erro durante a comunicação com o servidor:", str(erro))
            break

except Exception as erro:
    print("Erro ao conectar ao servidor:", str(erro))
finally:
    client_socket.close()
