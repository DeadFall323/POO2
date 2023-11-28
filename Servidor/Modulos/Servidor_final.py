import threading
import socket
import json
import mysql.connector as mysql
import geocoder
from datetime import datetime
from decimal import Decimal

########################################################################################################################
# Trecho relacionado a mudança de saldo do usuario


travar_acesso = threading.Lock()

def tabela_jogos(self):
    # PRECISA IR PARA O SERVIDOR
    travar_acesso.acquire()
    try:
        conexao = mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM jogos")
        dados = cursor.fetchall()
        conexao.close()

        dados_convertidos = []
        for tupla in dados:
            nova_tupla = []
            for item in tupla:
                if isinstance(item, Decimal):
                    nova_tupla.append(float(item))
                else:
                    nova_tupla.append(item)
            dados_convertidos.append(nova_tupla)

        dados_json = json.dumps(dados_convertidos)
        travar_acesso.release()
        return dados_json

    except Exception as e:
        print("Erro ao acessar o banco de dados da tabela", e)
        travar_acesso.release()
        return f"Erro: {str(e)}"

def atualiza_saldo(novo_saldo, email_destino):
    travar_acesso.acquire()
    try:
        conexao = mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b')
        cursor = conexao.cursor()
        cursor.execute("UPDATE usuarios SET saldo = %s WHERE email = %s", (novo_saldo, email_destino))
        conexao.commit()
        conexao.close()
        travar_acesso.release()

    except:
        travar_acesso.release()
        print("Erro ao atualizar saldo!")

def pega_saldo(email_destino):
    travar_acesso.acquire()
    try:
        conexao = mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b')
        cursor = conexao.cursor()
        cursor.execute("SELECT saldo FROM usuarios WHERE email = %s", (email_destino,))
        saldo = cursor.fetchone()[0]

        conexao.close()
        travar_acesso.release()
        return saldo

    except mysql.Error as err:
        travar_acesso.release()
        print(f"Erro ao buscar saldo: {err}")


def atualizar_saldo_por_email(email, novo_saldo):
    travar_acesso.acquire()
    try:
        with mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b') as conexao:
            cursor = conexao.cursor()

            cursor.execute("UPDATE usuarios SET saldo = %s WHERE email = %s", (novo_saldo, email))
            conexao.commit()
            conexao.close()
            print("Saldo atualizado com sucesso!")
            travar_acesso.release()


    except mysql.Error as err:
        travar_acesso.release()
        print(f"Erro ao atualizar saldo: {err}")

########################################################################################################################
def apaga_usuarios():
    travar_acesso.acquire()
    try:
        opcao = input("A SEGUINTE FUNÇÃO APAGA TODOS OS USARIOS CADASTRADOS, DESEJA CONTINUAR? (S/N): ")
        if opcao == "S" or opcao == "s":
            conn = mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b')
            cursor = conn.cursor()

            cursor.execute("DELETE FROM usuarios")

            conn.commit()
            conn.close()
            print("Dados da tabela 'usuarios' apagados com sucesso.")
            return True
        else:
            print("Nenhuma alteração feita.")
            travar_acesso.release()

    except mysql.Error as err:
        travar_acesso.release()
        print(f"Erro ao apagar os dados da tabela 'usuarios': {err}")
        return False


"""def limpar_base_sessao():
    try:
        with mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b') as conexao:
            cursor = conexao.cursor()

            cursor.execute("DELETE FROM sessao")
            conexao.commit()
            conexao.close()

    except mysql.Error as err:

        print(f"Erro ao limpar base de dados: {err}")"""


"""def adicionar_sessao(nome, email, nome_usuario, telefone, nascimento, rg, saldo):
    try:
        with mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b') as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "INSERT INTO sessao (nome, email, nome_usuario, telefone, nascimento, rg, saldo) VALUES ( %s, %s, %s, %s, %s, %s, %s)",
                (nome, email, nome_usuario, telefone, nascimento, rg, saldo))
            conexao.commit()
            conexao.close()
            print("Sessao criada com sucesso!")

    except mysql.Error as err:
        travar_acesso.release()
        print(f"Erro ao inserir dados: {err}")"""


def obter_informacoes_maquina():
    try:
        # Obter endereço IP
        hostname = socket.gethostname()
        endereco_ip = socket.gethostbyname(hostname)

        # Obter informações de localização com base no IP
        localizacao = geocoder.ip(endereco_ip)

        return {
            "endereco_ip": endereco_ip,
            "localizacao": localizacao.address
        }

    except Exception as e:
        travar_acesso.release()
        print(f"Erro ao obter informações da máquina: {str(e)}")
        return None


def verifica_existe(email, nome_usuario, telefone, rg):
    travar_acesso.acquire()
    try:
        conexao = mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b')
        cursor = conexao.cursor()
        cursor.execute(
            'SELECT * FROM usuarios WHERE email = %s OR nome_usuario = %s OR telefone = %s OR rg = %s',
            (email, nome_usuario, telefone, rg))
        resultado = cursor.fetchone()
        conexao.commit()
        conexao.close()
        travar_acesso.release()

        if resultado is not None:
            print("Usuario ja cadastrado!")
            return False
        else:
            return True

    except mysql.Error as err:
        travar_acesso.release()
        print(f"Erro ao inserir dados: {err}")
        return False

def cadastra_usuario(nome, email, nome_usuario, telefone, senha, nascimento, rg):
    travar_acesso.acquire()
    try:
        conn = mysql.connect(host='localhost', database='pooii', user='root', password='20pmto4b')
        cursor = conn.cursor()

        data_nascimento = datetime.strptime(nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')

        cursor.execute(
            """INSERT INTO usuarios(nome, email, nome_usuario, telefone, senha, nascimento, rg) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (nome, email, nome_usuario, telefone, senha, data_nascimento, rg))
        conn.commit()
        conn.close()
        travar_acesso.release()
        return True

    except mysql.Error as err:
        travar_acesso.release()
        print(f"Erro ao inserir dados: {err}")
        return False


def associar_jogo_usuario(id_usuario, id_jogo):
    travar_acesso.acquire()
    try:
        conn = mysql.connect(host='localhost', database='pooii', user='root', password='20pmto4b')
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO usuarios_jogos(id_usuario, id_jogo) VALUES (%s, %s)""", (id_usuario, id_jogo)
        )
        conn.commit()
        conn.close()
        travar_acesso.release()
        return True

    except mysql.Error as err:
        travar_acesso.release()
        print(f"Erro ao associar jogo e usuário: {err}")
        return False


def autenticar_usuario(ver_email, ver_senha):
    travar_acesso.acquire()
    # Prepara para nova sessão
    try:
        conexao = mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b')
        cursor = conexao.cursor()
        print("Verificando credenciais...")
        print("Email:", ver_email)
        print("Senha:", ver_senha)

        cursor.execute('SELECT * FROM usuarios WHERE email = %s AND senha = %s', (ver_email, ver_senha))
        resultado = cursor.fetchone()
        conexao.commit()
        conexao.close()
        travar_acesso.release()
        print("Resultado:", resultado)

        if ver_email == "admin" and ver_senha == "admin":


            return True

        elif resultado is not None and resultado[2] == ver_email and resultado[5] == ver_senha:


            return True

        else:
            print("Usuario nao cadastrado!")
            return False

    except mysql.Error as err:
        travar_acesso.release()
        print(f"Erro ao inserir dados: {err}")
        return False


class ClienteThread(threading.Thread):
    def __init__(self, clientAddress, clientesocket):
        threading.Thread.__init__(self)
        self.csocket = clientesocket
        self.name = ''
        self.addr = clientAddress
        print("Aguardando nova conexão...")
        print(50 * '-')
        print(obter_informacoes_maquina())
        print(50*'-')

    def run(self):
        # self.name = self.csocket.recv(1024).decode()
        # print(self.name, "se conectou!")
        # recebe = ''
        while True:
            # Recebe parametros(operacao/nome/ senha)
            print("Aguardando nova conexão...")
            data = self.csocket.recv(1024)
            recebe = data.decode()

            if not recebe:
                print("Conexão encerrada com Cliente")
                break
            # Separa os dados
            recebe = recebe.split(',')
            # Se não receber 2 dados, encerra a conexão
            if len(recebe) != 3 :
                print("Dados inválidos")
                self.csocket.close()
            else:

                operacao = recebe[0]
                print("Operação:", operacao)
                ################################ REQUISIÇÕES ACEITAS PELO SERVIDOR ##################################

                if recebe[0] == 'desconectar':
                    self.csocket.close()
                    print('Cliente se ', self.addr, 'Desconectou...')
                    break

                elif recebe[0] == "requisita_sessao":
                    print("Requisita sessao")
                    pass
                    """envia = str(pegar_dados_sessao())
                    print("DADOS DA SESSAO:", envia)
                    if envia is not None:
                        self.csocket.send(envia.encode())
                        print("Sessao enviada")
                        self.csocket.close()
                        print('Cliente se ', self.addr, 'Desconectou...')
                        break
                    else:
                        print("Erro ao obter sessão")
                        envia = '0'
                        self.csocket.send(envia.encode())
                        break"""

                elif recebe[0] == 'requisita_tabela_jogos':
                    print("Requisita tabela de jogos")
                    # IMPORTANTE IMPLEMENTAR OS JOGOS DOS USUARIOS ESPECIFICOS
                    # UTILIZAR AS MENSAGENS AUXILIARES PARA IDENTIFICAR O USUARIO

                    envia = str(tabela_jogos(self))

                    print(envia)
                    self.csocket.send(envia.encode())
                    print("Tabela enviada")
                    self.csocket.close()
                    print('Cliente se ', self.addr, 'Desconectou...')
                    break

                elif recebe[0] == 'requisita_saldo':
                    print("Requisita saldo do usuario atual")
                    saldo_atual = pega_saldo(recebe[1])
                    envia = str(saldo_atual)
                    print("saldo enviado:",envia)
                    self.csocket.send(envia.encode())
                    self.csocket.close()
                    print('Cliente se ', self.addr, 'Desconectou...')
                    break

                elif operacao == 'mudar_saldo':
                    print("Mudar saldo solicitado")
                    # saldo
                    msg1 = recebe[1]
                    print("msg1:", msg1)
                    # destino
                    msg2 = recebe[2]
                    print("msg2:", msg2)
                    if msg1 == "20":
                        print("Adicionar 20")

                        saldo_obtido = pega_saldo(msg2)
                        saldo_atual = int(saldo_obtido)
                        saldo_atual += 20

                        atualizar_saldo_por_email(msg2, saldo_atual)

                        envia = '1'
                        self.csocket.send(envia.encode())
                        print("{} tem um novo saldo de: R${},00:".format(msg2, saldo_atual))
                        break

                    elif msg1 == "50":
                        print("Adicionar 50")

                        saldo_obtido = pega_saldo(msg2)
                        saldo_atual = int(saldo_obtido)
                        saldo_atual += 50

                        atualizar_saldo_por_email(msg2, saldo_atual)

                        envia = '1'
                        self.csocket.send(envia.encode())
                        print("{} tem um novo saldo de: R${},00:".format(msg2, saldo_atual))
                        break

                    elif msg1 == "100":
                        print("Adicionar 100")

                        saldo_obtido = pega_saldo(msg2)
                        saldo_atual = int(saldo_obtido)
                        saldo_atual += 100

                        atualizar_saldo_por_email(msg2, saldo_atual)

                        envia = '1'
                        self.csocket.send(envia.encode())
                        print("{} tem um novo saldo de: R${},00:".format(msg2, saldo_atual))
                        break



                    elif msg1 == "200":
                        print("Adicionar 200")

                        saldo_obtido = pega_saldo(msg2)
                        saldo_atual = int(saldo_obtido)
                        saldo_atual += 200

                        atualizar_saldo_por_email(msg2, saldo_atual)

                        envia = '1'
                        self.csocket.send(envia.encode())
                        print("{} tem um novo saldo de: R${},00:".format(msg2, saldo_atual))
                        break
                    else:
                        print("Erro ao contactar servidor")
                        envia = '0'
                        self.csocket.send(envia.encode())
                        break

                elif operacao == 'login':

                    print("Login solicitado")
                    email = recebe[1]
                    senha = recebe[2]
                    print("email:", email)
                    print("senha", senha)
                    if autenticar_usuario(email, senha):
                        envia = '1'
                        self.csocket.send(envia.encode())
                        print("Login realizado com sucesso!")
                        break
                    envia = '0'
                    self.csocket.send(envia.encode())
                    self.csocket.close()
                    break

                elif operacao == 'cadastrar':
                    print("Cadastrar novo usuario")
                    msg1 = recebe[1]
                    msg2 = recebe[2]

                    if msg1 == "ignore" or msg2 == "ignore":
                        print("if msg1 and msg2 == ignore")
                        # ESSA CONFIRMAÇÃO É PARA O SERVIDOR SABER QUE O CLIENTE QUER CADASTRAR
                        # Dessa forma envia a confirmação para o cliente
                        # Depois o cliente vai enviar os dados que serão cadastrados
                        # 1 == "Pode mandar os dados"
                        envia = '1'
                        self.csocket.send(envia.encode())
                        # Agora o servidor recebe os dados que serão cadastrados
                        data = self.csocket.recv(1024)
                        recebe = data.decode('utf-8')

                        # PRINTA OS PARAMETROS RECEBIDOS
                        # Nome, email, nome_usuario, telefone, senha, nascimento, rg
                        print(recebe)

                        if not recebe:
                            print("Conexão encerrada com Cliente")
                            break

                        # Separa os dados
                        recebe = recebe.split(',')

                        if len(recebe) != 7:
                            print("Dados inválidos")
                            self.csocket.close()

                        else:
                            nome = recebe[0]
                            email = recebe[1]
                            nome_usuario = recebe[2]
                            telefone = recebe[3]
                            senha = recebe[4]
                            nascimento = recebe[5]
                            rg = recebe[6]
                            print("nome:", nome)
                            print("email:", email)
                            print("nome_usuario:", nome_usuario)
                            print("telefone:", telefone)
                            print("senha:", senha)
                            print("nascimento:", nascimento)
                            print("rg:", rg)

                            if verifica_existe(email, nome_usuario, telefone, rg):
                                # SE  VERDADE
                                # CADASTRA O USUARIO

                                if cadastra_usuario(nome, email, nome_usuario, telefone, senha, nascimento, rg):
                                    envia = '1'
                                    self.csocket.send(envia.encode())
                                    print("Usuario cadastrado com sucesso!")
                                    break

                                else:
                                    envia = '0'
                                    self.csocket.send(envia.encode())
                                    print("Erro ao cadastrar usuario!")
                                    break

                            else:
                                envia = '2'
                                self.csocket.send(envia.encode())
                                print("Usuario ja cadastrado!")
                                break

                        print("break final")
                        break

                else:
                    print("Operação inválida")
                    envia = 'ERROR'
                    self.csocket.send(envia.encode())
                    self.csocket.close()
                    break

if __name__ == '__main__':
    localhost = ''
    port = 32323
    addr = (localhost, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print(50*"-")
    print('Servidor iniciado!')
    print("IP:", localhost)
    print("Porta:", port)
    print(50 * "-")
    while True:
        server.listen(20)
        clientsock, clientAddress = server.accept()
        newthread = ClienteThread(clientAddress, clientsock)
        newthread.start()
