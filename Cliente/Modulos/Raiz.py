import socket
import json
import threading
import time as temporizador
import sqlite3



from Qt import *

"""

SUMARIO: Modulo que contem a classe Raiz, que é a classe base de todas as outras classes do programa.

ORDEM DAS TELAS:

    1 - Tela_INICIO
    2 - Tela_login_user OU Tela_login_cadastro
    3 - Tela_principal
    4 - Tela_jogo
    5 - Tela_Loja
    6 - Tela_Configuracoes
    7 - Tela_Sobre
    8 - Tela_adicionar_fundos

"""


# Função global
def obter_endereco_ip():
    hostname = socket.gethostname()
    endereco_ip = socket.gethostbyname(hostname)
    return endereco_ip


# Funções de banco de dados local

def criar_banco_dados():
    con = sqlite3.connect('Dados.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS conexao (IP text, Porta text)")
    con.commit()
    con.close()


def conecta_servidor():
    IP = ''
    Porta = ''
    con = sqlite3.connect('Dados.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM conexao")
    for linha in cursor.fetchall():
        IP = linha[0]
        Porta = int(linha[1])
    cursor.close()
    con.close()
    if IP == '' or Porta == '':
        print("Não foi possivel conectar ao servidor")
        print(50*"-")
        print("Ip e porta Nulos")
        print(50 * "-")
        ip = obter_endereco_ip()
        porta_padrao = 32323
        print("Ip e porta padrão:")
        print("IP:", ip)
        print("Porta:", porta_padrao)
        salva_servidor(ip, porta_padrao)
        return ip, porta_padrao

    print("conectando:")
    print("ip:", IP)
    print("porta:", Porta)
    return IP, Porta

def salva_servidor(ip, porta):
    con = sqlite3.connect('Dados.db')
    cursor = con.cursor()
    # Isso limpa as conexões anteriores
    cursor.execute("DELETE FROM conexao")
    # Já isso, adiciona a nova conexão
    cursor.execute("INSERT INTO conexao VALUES (?, ?)", (ip, porta))
    con.commit()
    con.close()
    return True

########################################################################################################################
# IMPORTAÇÕES:
# Tela_inicio
# from Cliente.Modulos.Templates.ui_Tela_inicial import Ui_Tela_inicio
from Templates.ui_Tela_inicial import Ui_Tela_inicio

# Tela_configurar_conexao
#from Cliente.Modulos.Templates.ui_Tela_configurar_server import Ui_Tela_configurar_server
from Templates.ui_Tela_configurar_server import Ui_Tela_configurar_server

# Tela_login_user
# from Cliente.Modulos.Templates.ui_Tela_Login import Ui_tela_login
from Templates.ui_Tela_Login import Ui_tela_login

# Tela_login_redefinir_senha
#from Cliente.Modulos.Templates.ui_Tela_redefinir_senha import Ui_Ui_tela_login_redefinir_senha
from Templates.ui_Tela_redefinir_senha import Ui_Ui_tela_login_redefinir_senha

# Tela_login_redefinir_senha_2
#from Cliente.Modulos.Templates.ui_Tela_redefinir_senha_2 import Ui_Ui_tela_login_redefinir_senha_2
from Templates.ui_Tela_redefinir_senha_2 import Ui_Ui_tela_login_redefinir_senha_2

# Tela_login_cadastro
# from Cliente.Modulos.Templates.ui_Tela_cadastrar_usuario import Ui_tela_cadastrar_usuario
from Templates.ui_Tela_cadastrar_usuario import Ui_tela_cadastrar_usuario

# Tela_menu_principal
#from Cliente.Modulos.Templates.ui_Tela_principal import Ui_Tela_principal
from Templates.ui_Tela_principal import Ui_Tela_principal

# Tela_adicionar_fundos
# from Cliente.Modulos.Templates.ui_Tela_adicionar_fundos import Ui_adicionar_fundos
from Templates.ui_Tela_adicionar_fundos import Ui_adicionar_fundos

# Tela_de_Ajuda


########################################################################################################################


# Classes:
# 1 - Tela_inicio
class Tela_configurar_conexao(QMainWindow):
    def __init__(self, tela_login_inst, *args, **argvs):
        super(Tela_configurar_conexao, self).__init__(*args, **argvs)

        self.tela_login_inst = tela_login_inst
        self.ui = Ui_Tela_configurar_server()
        self.ui.setupUi(self)

        self.ui.checkBox.setCheckable(False)  # Impede que o usuário altere o checkbox
        self.ui.checkBox_2.setCheckable(False)  # Impede que o usuário altere o checkbox

        # Verifica Servidor
        if self.verifica():
            self.ui.checkBox.setCheckState(True)
        else:
            self.ui.checkBox.setCheckState(False)

        # Verifica Banco de dados
        if self.verifica_DB():
            self.ui.checkBox_2.setCheckState(True)
        else:
            self.ui.checkBox_2.setCheckState(False)

        self.ui.pushButton.clicked.connect(self.verifica)
        self.ui.pushButton_3.clicked.connect(self.voltar)
        # Retorna o ip do computador
        self.ui.lineEdit.setText(obter_endereco_ip())

    def verifica(self):
        ip = self.ui.lineEdit.text()
        port = self.ui.lineEdit_2.text()
        print("IP:", ip)
        print("Port:", port)
        try:
            addr = ((ip, int(port)))
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if client_socket.connect(addr):
                salva_servidor(ip, port)
                QMessageBox.about(self, "Servidor", "Servidor conectado com sucesso!")
                client_socket.close()
                self.close()
                self.tela_login_inst.show()
                return True
            else:
                QMessageBox.about(self, "Servidor", "Não foi possivel conectar ao servidor!")
                return False

        except Exception as erro:
            self.close()
            QMessageBox.about(self, "Servidor", "Não foi possivel conectar ao servidor!")
            print(str(erro))
            return False

    def verifica_DB(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)

            while True:
                operacao = 'verifica_DB'
                msg1 = 'ignore_verifica_DB'
                msg2 = 'ignore_verifica_DB'
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))

                recebe = client_socket.recv(1024)
                Status_DB = recebe.decode('utf-8')

                if Status_DB == '1':
                    return True

                else:
                    return False

        except Exception as erro:
            print(str(erro))
            return False

    def voltar(self):
        self.close()
        self.tela_login_inst.show()


class Tela_login(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_login, self).__init__(*args, **argvs)
        self.ui = Ui_Tela_inicio()
        self.ui.setupUi(self)

        criar_banco_dados()

        def verifica_conexoes():
            # Verifica Servidor
            if self.verifica_servidor():
                self.ui.checkBox.setCheckState(True)
            else:
                self.ui.checkBox.setCheckState(False)

            # Verifica Banco de dados
            if self.verifica_DB():
                self.ui.checkBox_2.setCheckState(True)

            else:
                self.ui.checkBox_2.setCheckState(False)

        verifica_conexoes()
        self.ui.checkBox.setCheckable(False)  # Impede que o usuário altere o checkbox
        self.ui.checkBox_2.setCheckable(False)  # Impede que o usuário altere o checkbox

        self.ui.pushButton.clicked.connect(self.abrir_login)
        self.ui.pushButton_2.clicked.connect(self.abrir_cadastrar)
        self.ui.pushButton_3.clicked.connect(self.sair)
        self.ui.pushButton_4.clicked.connect(self.configura_conexao)

        self.ui.checkBox.setCheckable(False)  # Impede que o usuário altere o checkbox
        self.ui.checkBox_2.setCheckable(False)  # Impede que o usuário altere o checkbox

    def configura_conexao(self):
        self.window = Tela_configurar_conexao(self)
        self.window.show()

    def verifica_servidor(self):
        addr = conecta_servidor()
        print("Verificando servidor...")
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            client_socket.close()
            return True
        except Exception as erro:
            print(str(erro))
            return False

    def verifica_DB(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)

            while True:
                operacao = 'verifica_DB'
                msg1 = 'ignore_verifica_DB'
                msg2 = 'ignore_verifica_DB'
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))

                recebe = client_socket.recv(1024)
                Status_DB = recebe.decode('utf-8')

                if Status_DB == '1':
                    return True
                else:
                    return False
        except Exception as erro:
            print("Erro ao verificar banco de dados:",str(erro))
            return False

    def abrir_cadastrar(self):
        self.close()
        self.window = Cadastrar_usuario(self)
        self.window.show()

    def abrir_login(self):
        self.close()
        self.window = Tela_login_user(self)
        self.window.show()

    def sair(self):
        self.close()
        exit(323)

# 2 - Tela_login_user
class Tela_login_user(QMainWindow):
    def __init__(self, tela_login_inst, *args, **argvs):
        super(Tela_login_user, self).__init__(*args, **argvs)
        self.tela_login_inst = tela_login_inst
        self.ui = Ui_tela_login()

        self.usuario_ativo = None
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.redefinir_senha)
        self.ui.pushButton_2.clicked.connect(self.efetuar_login)
        self.ui.pushButton_3.clicked.connect(self.voltar)

    def verifica_servidor(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            client_socket.close()
            return True
        except Exception as erro:
            print(str(erro))
            return False

    def efetuar_login(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            print("Conectado ao servidor...")
            while True:
                email = self.ui.lineEdit.text()
                senha = self.ui.lineEdit_2.text()
                operacao = 'login'
                comando = operacao + "," + email + "," + senha
                client_socket.send(comando.encode('utf-8'))

                print("Dados de login enviados")
                recebe = client_socket.recv(1024)
                print(recebe.decode('utf-8'))

                if recebe.decode('utf-8') == '1':
                    print("Login encontrado")
                    self.usuario_ativo = email
                    self.window = Tela_inicial(self, self.usuario_ativo)
                    self.window.show()
                    self.close()
                    client_socket.close()

                if recebe.decode('utf-8') == '2':
                    print("Cadastrar novo usuario")

                elif recebe.decode('utf-8') == '0':
                    QMessageBox.about(self, "Erro", "Usuario ou senha incorretos")
                    client_socket.close()
                    break
                else:
                    print("Erro ao contactar servidor")
                    client_socket.close()
                    break

        except Exception as erro:
            print(str(erro))
            QMessageBox.about(self, "Erro", "Não foi possivel conectar ao servidor!")

    def redefinir_senha(self):
        print("Redefinir senha")
        self.window = Tela_login_redefinir_senha(self.tela_login_inst)
        self.window.show()
        self.close()

    def voltar(self):
        self.close()
        self.tela_login_inst.show()


class Tela_login_redefinir_senha(QMainWindow):
    def __init__(self, tela_login_inst, *args, **argvs):
        super(Tela_login_redefinir_senha, self).__init__(*args, **argvs)
        self.tela_login_inst = tela_login_inst
        self.ui = Ui_Ui_tela_login_redefinir_senha()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.redefinir_senha)
        self.ui.pushButton_3.clicked.connect(self.voltar)

    def redefinir_senha(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            while True:
                self.email = self.ui.lineEdit.text()

                operacao = 'verificar_email_cadastrado'
                senha = "ignore_verificar_email_cadastrado"

                comando = operacao + "," + self.email + "," + senha
                print("Email enviado:", self.email)
                client_socket.send(comando.encode('utf-8'))

                recebe = client_socket.recv(1024)
                print(recebe.decode('utf-8'))

                if recebe.decode('utf-8') == '1':
                    print("email encontrado")
                    self.email_redefinir = self.email
                    self.window = Tela_login_redefinir_senha_2(self, self.email_redefinir)
                    self.window.show()
                    self.close()
                    client_socket.close()

                elif recebe.decode('utf-8') == '0':
                    QMessageBox.about(self, "Erro", "Email não encontrado")
                    client_socket.close()
                    break

                else:
                    print("Erro ao contactar servidor")
                    client_socket.close()
                    break

        except Exception as erro:
            print(str(erro))
            QMessageBox.about(self, "Erro", "Não foi possivel conectar ao servidor!")

    def voltar(self):
        self.close()
        self.tela_login_inst.show()


class Tela_login_redefinir_senha_2(QMainWindow):
    def __init__(self, tela_login_inst, email_redefinir, *args, **argvs):
        super(Tela_login_redefinir_senha_2, self).__init__(*args, **argvs)
        self.tela_login_inst = tela_login_inst
        self.ui = Ui_Ui_tela_login_redefinir_senha_2()
        self.ui.setupUi(self)
        self.email_redefinir = email_redefinir

        self.ui.pushButton_2.clicked.connect(self.voltar)
        self.ui.pushButton_3.clicked.connect(self.redefinir_senha)

    def redefinir_senha(self):
        self.ui.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            while True:

                # senha = self.ui.lineEdit.text()
                senha = self.ui.lineEdit.text()
                senha_conf = self.ui.lineEdit_2.text()

                if senha != senha_conf:
                    QMessageBox.about(self, "Erro", "Senhas não coincidem!")
                    self.ui.lineEdit.setText('')
                    self.ui.lineEdit_2.setText('')
                    self.ui.lineEdit.setFocus()

                operacao = 'redefinir_senha'
                comando = operacao + "," + self.email_redefinir + "," + senha
                client_socket.send(comando.encode('utf-8'))

                print("Dados de login enviados")
                recebe = client_socket.recv(1024)
                print(recebe.decode('utf-8'))

                if recebe.decode('utf-8') == '1':
                    print("Login encontrado")
                    self.usuario_ativo = self.email_redefinir
                    self.window = Tela_inicial(self, self.usuario_ativo)
                    self.window.show()
                    self.close()

                    client_socket.close()

                if recebe.decode('utf-8') == '2':
                    print("Cadastrar novo usuario")

                elif recebe.decode('utf-8') == '0':
                    QMessageBox.about(self, "Erro", "Usuario ou senha incorretos")
                    client_socket.close()
                    break
                else:
                    print("Erro ao contactar servidor")
                    client_socket.close()
                    break

        except Exception as erro:
            print(str(erro))
            QMessageBox.about(self, "Erro", "Não foi possivel conectar ao servidor!")

    def voltar(self):
        self.close()
        self.tela_login_inst.show()


# 3 - Tela_login_cadastro
class Cadastrar_usuario(QMainWindow):
    def __init__(self, tela_login_inst, *args, **argvs):
        super(Cadastrar_usuario, self).__init__(*args, **argvs)
        self.tela_login_inst = tela_login_inst
        self.ui = Ui_tela_cadastrar_usuario()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cadastrar)
        self.ui.pushButton_2.clicked.connect(self.voltar)

    def voltar(self):
        self.close()
        self.tela_login_inst.show()

    def cadastrar(self):
        nome = self.ui.lineEdit.text()
        email = self.ui.lineEdit_2.text()
        nome_usuario = self.ui.lineEdit_3.text()
        telefone = self.ui.lineEdit_7.text()
        senha = self.ui.lineEdit_4.text()
        ########-----
        # conf_senha = self.ui..text()
        conf_senha = senha
        ########-----
        # nascimento = QDate.fromString(self.ui.Nascimento.date().toString(), 'yyyy-MM-dd').toString('dd/MM/yyyy')
        nascimento = self.ui.lineEdit_5
        rg = self.ui.lineEdit_6.text()

        print(
            "Nome:{} Email:{} Nome_usuario:{} telefone:{} senha:() conf_senha() Nascimento:{} RG:{}".format(nome, email,
                                                                                                            nome_usuario,
                                                                                                            telefone,
                                                                                                            senha,
                                                                                                            conf_senha,
                                                                                                            nascimento,
                                                                                                            rg))
        if nome == '' or email == '' or nome_usuario == '' or telefone == '' or senha == '' or rg == '':
            QMessageBox.about(self, "Cadastro", "Preencha todos os campos!")

        else:
            if senha != conf_senha:
                QMessageBox.about(self, "Cadastro", "Senhas não coincidem!")
                # self.ui.Senha_user.setText('')
                # self.ui.Senha_verifica.setText('')
                # self.ui.Senha_user.setFocus()

            if senha == conf_senha:
                try:

                    addr = conecta_servidor()
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect(addr)
                    print("Conectado ao servidor...")

                    while True:

                        # Defina as variáveis
                        operacao = 'cadastrar'
                        env_nome = nome
                        env_email = email
                        env_nome_usuario = nome_usuario
                        env_telefone = telefone
                        env_senha = senha
                        env_nascimento = '30/03/2001'
                        env_rg = rg

                        # Envia requisição de cadastro ao servidor
                        var1 = 'ignore'
                        var2 = 'ignore'
                        comando = f"{operacao},{var1}, {var2}"
                        client_socket.send(comando.encode('utf-8'))

                        # Recebe a resposta para enviar os dados

                        recebe = client_socket.recv(1024)
                        if recebe.decode('utf-8') == '1':
                            comando = f"{env_nome},{env_email},{env_nome_usuario},{env_telefone},{env_senha},{env_nascimento},{env_rg}"
                            print(comando)
                            client_socket.send(comando.encode('utf-8'))
                            print("Dados de cadastro enviados")

                            # Aguarda resposta do servidor
                            recebe = client_socket.recv(1024)
                            print(recebe.decode('utf-8'))
                            if recebe.decode('utf-8') == '1':
                                print("Cliente foi cadastrado")
                                QMessageBox.about(self, "Cadastro", "Cadastro feito com sucesso!")
                                self.close()
                                self.tela_login_inst.show()
                                client_socket.close()

                            elif recebe.decode('utf-8') == '0':
                                QMessageBox.about(self, "Cadastro", "Senhas não coincidem!")

                            elif recebe.decode('utf-8') == '2':
                                QMessageBox.about(self, "Erro", "Usuario ja cadastrado")
                                self.close()
                                self.tela_login_inst.show()
                                client_socket.close()
                                break

                            else:
                                print("Erro ao contactar servidor")
                                client_socket.close()
                                break

                        ##############################################################
                        # SE REMOVER O CODIGO CRASHA
                        # "TIME QUE ESTA VENCENDO NÃO SE MUDA"
                        client_socket.send(comando.encode('utf-8'))
                        print("Dados de cadastro enviados")

                        # Aguarda resposta do servidor
                        recebe = client_socket.recv(1024)
                        print("resposta do cadastro:")
                        print(recebe.decode('utf-8'))

                        if recebe.decode('utf-8') == '1':
                            print("Cliente foi cadastrado")
                            QMessageBox.about(self, "Cadastro", "Cadastro feito com sucesso!")
                            self.close()
                            client_socket.close()

                        if recebe.decode('utf-8') == '0':
                            QMessageBox.about(self, "Cadastro", "Senhas não coincidem!")

                        elif recebe.decode('utf-8') == '2':
                            QMessageBox.about(self, "Erro", "Usuario ja cadastrado")
                            client_socket.close()
                            break

                        else:
                            print("Erro ao contactar servidor")
                            client_socket.close()
                            break
                        ##############################################################

                except Exception as erro:
                    print(str(erro))


# 4 - Tela_principal

class Tela_inicial(QMainWindow):
    def __init__(self, tela_login_inst, usuario_ativo, *args, **argvs):
        super(Tela_inicial, self).__init__(*args, **argvs)
        self.tela_login_inst = tela_login_inst
        self.usuario_ativo = usuario_ativo
        self.ui = Ui_Tela_principal()
        self.ui.setupUi(self)

        self._thread_ativa = True

        self.ui.Redireciona_loja.clicked.connect(self.redireciona_loja)
        self.ui.Abr_lista_amigos.clicked.connect(self.abrir_biblioteca)  # -> BIBLIOTECA
        self.ui.Perfil_usuario.clicked.connect(self.perfil_usuario)
        # self.ui.stackedWidget.setCurrentWidget(self.ui.Loja)
        self.ui.Sair.clicked.connect(self.sair)

        self.ui.adicionar_money.clicked.connect(self.adicionar_fundos)

        # TABELA
        self.atualizar_tabela()
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.clicked.connect(self.botao_da_tabela)

        self.saldo_lcd = self.findChild(QtWidgets.QLCDNumber, 'Saldo')
        # self.saldo_lcd.setDigitCount(10)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.atualizar_saldo)

        self.timer.start(7000)
        self.valor = self.requisita_saldo()
        self.saldo_lcd.display(self.valor)

        print("------------------")
        print("Usuario ativo:", self.usuario_ativo)
        print("------------------")


        # Inicia a thread para atualizar a tabela

        self.thread_tabela = threading.Thread(target=self.loop_atualizacao_tabela)
        self.thread_tabela.daemon = True  # Define como thread 'daemon' para terminar com o programa principal
        self.thread_tabela.start()

    def loop_atualizacao_tabela(self):
        while self._thread_ativa:  # Loop é executado enquanto a variável de controle estiver True
            self.atualizar_tabela()
            temporizador.sleep(5)

    def atualizar_tabela(self):
        while True:
            self.atualizar_tabela()  # Chama o método da classe para atualizar a tabela
            temporizador.sleep(5)  # Aguarda 5 segundos antes da próxima atualização



    def botao_da_tabela(self, item):
        row = item.row()
        col = item.column()
        item_value = self.ui.tableWidget.item(row, col).text()
        if col == 0:
            print(f"Item clicado: {item_value}")
            # NÂO FUNCIONANDO
            """# caminho_executavel = os.path.abspath('Jogos/jogo.exe')
            caminho_executavel = r"D:\Área de Trabalho\Jogos\jogo1.exe"
            subprocess.Popen([caminho_executavel])"""
        else:
            print(f"Item clicado: {item_value}")

    def requisita_tabela_jogos(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)

            while True:
                operacao = 'requisita_tabela_jogos'
                msg1 = 'ignore_requisita_tabela_jogos1'
                msg2 = 'ignore_requisita_tabela_jogos2'
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))

                recebe = client_socket.recv(1024)
                tabela = recebe.decode('utf-8')
                texto_corrigido = tabela.encode('utf-8').decode('unicode-escape')
                print("Tabela recebida:", texto_corrigido)

                # Convertendo a string para uma estrutura de dados Python usando json.loads
                dados = json.loads(tabela)

                # Processamento dos dados
                dados_processados = []
                for tupla in dados:
                    novo_registro = list(tupla[1:])  # Excluindo o primeiro elemento (ID)
                    # Convertendo Decimals para float
                    novo_registro[-2] = float(novo_registro[-2])
                    novo_registro[-1] = float(novo_registro[-1])
                    dados_processados.append(novo_registro)

                return dados_processados

        except Exception as erro:
            print(str(erro))

    def requisita_saldo(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            while True:
                operacao = 'requisita_saldo'
                msg1 = self.usuario_ativo
                msg2 = 'ignore_requisita_saldo2'
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))

                recebe = client_socket.recv(1024)
                valor_saldo = recebe.decode('utf-8')
                return valor_saldo

        except Exception as erro:
            print(str(erro))

    def atualizar_saldo(self):

        novo_saldo = self.requisita_saldo()
        self.saldo_lcd.display(novo_saldo)
        print("Saldo:", novo_saldo)

    def atualizar_tabela(self):
        try:
            dados = self.requisita_tabela_jogos()
            self.ui.tableWidget.setRowCount(len(dados))  # Define o número de linhas com base na quantidade de dados

            for row_index, row_data in enumerate(dados, start=0):  # Começa do índice 0
                for col_index, cell_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(cell_data))
                    self.ui.tableWidget.setItem(row_index, col_index, item)  # Ajusta o índice da linha na tabela

            self.ui.tableWidget.update()

        except Exception as e:
            print("Erro ao atualizar tabela:", e)

    def redireciona_loja(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Loja)
        print("Redireciona loja")

    def abrir_biblioteca(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Abr_lista_amigos)
        print("Biblioteca")

    def perfil_usuario(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Perfil_usuario)
        print("Perfil do usuario")

    def adicionar_fundos(self):
        print("Adicionar fundos")
        self.tela_adicionar_fundos = Tela_adicionar_fundos(usuario_ativo=self.usuario_ativo)
        self.tela_adicionar_fundos.show()
        self.requisita_saldo()

    def sair(self):
        self._thread_ativa = False
        self.thread_tabela.join()  # Aguarda a thread terminar

        self.timer.start(False)  # Para o timer

        print("Saindo...")
        self.close()
        self.tela_login_inst.show()


# 5 - Tela_adicionar_fundos
class Tela_adicionar_fundos(QMainWindow):
    def __init__(self, *args, usuario_ativo, **argvs):
        super(Tela_adicionar_fundos, self).__init__(*args, **argvs)
        self.ui = Ui_adicionar_fundos()
        self.ui.setupUi(self)

        self.ui.cancelar.clicked.connect(self.voltar)
        self.ui.adc_20.clicked.connect(self.adicionar_20)
        self.ui.adc_50.clicked.connect(self.adicionar_50)
        self.ui.adc_100.clicked.connect(self.adicionar_100)
        self.ui.adc_200.clicked.connect(self.adicionar_200)

        self.usuario_ativo = usuario_ativo

    def adicionar_20(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            print("Conectado ao servidor...")

            while True:
                operacao = 'mudar_saldo'
                msg1 = '20'
                msg2 = self.usuario_ativo
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))
                print("operação enviada")
                # recebe o retorno da solicitação de mudar_saldo

                recebe = client_socket.recv(1024)
                print(recebe.decode('utf-8'))

                if recebe.decode('utf-8') == '0':
                    print("Não foi possível adicionar saldo")

                elif recebe.decode('utf-8') == '1':
                    print("Saldo adicionado com sucesso")
                    QMessageBox.about(self, "Depósito", "R$ 20,00 adicionados!")
                    self.close()
                    client_socket.close()
                    break

                else:
                    print("Erro ao contactar servidor")
                    client_socket.close()
                    break

        except Exception as erro:
            print(str(erro))

    def adicionar_50(self):

        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            print("Conectado ao servidor...")

            while True:
                operacao = 'mudar_saldo'
                msg1 = '50'
                msg2 = self.usuario_ativo
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))
                print("operação enviada")
                # recebe o retorno da solicitação de mudar_saldo

                recebe = client_socket.recv(1024)
                print(recebe.decode('utf-8'))

                if recebe.decode('utf-8') == '0':
                    print("Não foi possível adicionar saldo")

                elif recebe.decode('utf-8') == '1':
                    print("Saldo adicionado com sucesso")
                    QMessageBox.about(self, "Depósito", "R$ 50,00 adicionados!")
                    self.close()
                    client_socket.close()
                    break

                else:
                    print("Erro ao contactar servidor")
                    client_socket.close()
                    break

        except Exception as erro:
            print(str(erro))

    def adicionar_100(self):

        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            print("Conectado ao servidor...")

            while True:
                operacao = 'mudar_saldo'
                msg1 = '100'
                msg2 = self.usuario_ativo
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))
                print("operação enviada")
                # recebe o retorno da solicitação de mudar_saldo

                recebe = client_socket.recv(1024)
                print(recebe.decode('utf-8'))

                if recebe.decode('utf-8') == '0':
                    print("Não foi possível adicionar saldo")

                elif recebe.decode('utf-8') == '1':
                    print("Saldo adicionado com sucesso")
                    QMessageBox.about(self, "Depósito", "R$ 100,00 adicionados!")
                    self.close()
                    client_socket.close()
                    break

                else:
                    print("Erro ao contactar servidor")
                    client_socket.close()
                    break

        except Exception as erro:
            print(str(erro))

    def adicionar_200(self):

        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            print("Conectado ao servidor...")

            while True:
                operacao = 'mudar_saldo'
                msg1 = '200'
                msg2 = self.usuario_ativo
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))
                print("operação enviada")
                # recebe o retorno da solicitação de mudar_saldo

                recebe = client_socket.recv(1024)
                print(recebe.decode('utf-8'))

                if recebe.decode('utf-8') == '0':
                    print("Não foi possível adicionar saldo")

                elif recebe.decode('utf-8') == '1':
                    print("Saldo adicionado com sucesso")
                    QMessageBox.about(self, "Depósito", "R$ 200,00 adicionados!")
                    self.close()
                    client_socket.close()
                    break

                else:
                    print("Erro ao contactar servidor")
                    client_socket.close()
                    break

        except Exception as erro:
            print(str(erro))

    def voltar(self):
        print("Voltar")
        self.close()


