from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
import socket
import json
import threading


# Função global
def obter_endereco_ip():
    hostname = socket.gethostname()
    endereco_ip = socket.gethostbyname(hostname)
    return endereco_ip

def conecta_servidor():
    #ip = '192.168.1.78'
    ip = "localhost"
    port = 32323
    addr = ((ip, port))
    return addr

"""
###
SUMARIO: Modulo que contem a classe Raiz, que e a classe base de todas as outras classes do programa.

ORDEM DAS TELAS:

    1 - Tela_INICIO
    2 - Tela_login_user OU Tela_login_cadastro
    3 - Tela_principal
    4 - Tela_jogo
    5 - Tela_Loja
    6 - Tela_Configuracoes
    7 - Tela_Sobre
    8 - Tela_adicionar_fundos

###
IMPORTAÇÕES:
"""
# Tela_inicio
# from Modulos.Templates.Tela_inicio import *
from Templates.Tela_inicio import *

# from Cliente.Modulos.Templates.Tela_inicio import *

"""from Cliente.Modulos.Tela_login_cadastro import Cadastrar_usuario"""
"""from Cliente.Modulos.Tela_login_user import Tela_login_user"""

# Tela_login_user
from Templates.Tela_login_user import *
"""from Cliente.Modulos.Tela_menu_principal import Tela_inicial"""

# Tela_login_cadastro
from Templates.Tela_Cadastro import *

# Tela_menu_principal
"""from Cliente.Modulos.Parametros_Servidor import conecta_servidor"""
from Templates.Tela_Principal import *
"""from Cliente.Modulos.Tela_de_Ajuda import Tela_adm_menu as Tela_ajuda"""
"""from Cliente.Modulos.Tela_adicionar_fundos import Tela_adicionar_fundos as Tela_adicionar_fundos"""

# ERROR AQUI: RESOLVER PROBLEMA DE IMPORTAÇÃO CIRCULAR
# from Testes.adm.Tela_login_adm import Login_adm as Tela_login_adm

# Tela_adicionar_fundos
from Templates.Tela_Adicionar_fundos_user import *
"""from Cliente.Modulos.Parametros_Servidor import conecta_servidor"""
# Tela_de_Ajuda
from Templates.Tela_de_Ajuda import *

########################################################################################################################


# Classes:
# 1 - Tela_inicio
class Tela_login(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_login, self).__init__(*args, **argvs)
        self.ui = Ui_Tela_inicio()
        self.ui.setupUi(self)

        self.ui.Cadastrar_novo_user.clicked.connect(self.abrir_cadastrar)
        self.ui.Login_user.clicked.connect(self.abrir_login)
        self.ui.sair.clicked.connect(self.sair)
        self.verifica_servidor()

    def verifica_servidor(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)
            QMessageBox.about(self, "Servidor", "Servidor conectado com sucesso!")
            client_socket.close()
            return True

        except Exception as erro:
            QMessageBox.about(self, "Servidor", "Não foi possivel conectar ao servidor!")
            print(str(erro))
            return True

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
        exit(0)

# 2 - Tela_login_user
class Tela_login_user(QMainWindow):
    def __init__(self, tela_login_inst, *args, **argvs):
        super(Tela_login_user, self).__init__(*args, **argvs)
        self.tela_login_inst = tela_login_inst
        self.ui = Ui_Tela_login()

        self.usuario_ativo = None
        self.ui.setupUi(self)

        self.ui.Login.clicked.connect(self.efetuar_login)
      # self.ui.pushButton.clicked.connect(self.redefinir_senha)
        self.ui.Sair.clicked.connect(self.voltar)
        addr = conecta_servidor()
        #client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
                    self.usuario_ativo = email  # Corrigindo para self.usuario_ativo
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
        pass

    def voltar(self):
        self.close()
        self.tela_login_inst.show()

# 3 - Tela_login_cadastro
class Cadastrar_usuario(QMainWindow):
    def __init__(self, tela_login_inst, *args, **argvs):
        super(Cadastrar_usuario, self).__init__(*args, **argvs)
        self.tela_login_inst = tela_login_inst
        self.ui = Ui_Ui_Tela_Login_cadastro_user()
        self.ui.setupUi(self)
        self.ui.Cadastrar_usuario.clicked.connect(self.cadastrar)
        self.ui.Voltar.clicked.connect(self.voltar)

    def voltar(self):
        self.close()
        self.tela_login_inst.show()


    def cadastrar(self):
        nome = self.ui.Nome_completo.text()
        email = self.ui.Endereco_email.text()
        nome_usuario = self.ui.Nome_usuario.text()
        telefone = self.ui.Telefone.text()
        senha = self.ui.Senha_user.text()
        conf_senha = self.ui.Senha_verifica.text()
        nascimento = QDate.fromString(self.ui.Nascimento.date().toString(), 'yyyy-MM-dd').toString('dd/MM/yyyy')
        rg = self.ui.CPF.text()


        print("Nome:{} Email:{} Nome_usuario:{} telefone:{} senha:() conf_senha() Nascimento:{} RG:{}".format(nome, email, nome_usuario, telefone, senha, conf_senha, nascimento, rg))
        if nome == '' or email == '' or nome_usuario == '' or telefone == '' or senha == '' or conf_senha == '' or rg == '':
            QMessageBox.about(self, "Cadastro", "Preencha todos os campos!")

        else:
            if senha != conf_senha:
                QMessageBox.about(self, "Cadastro", "Senhas não coincidem!")
                self.ui.Senha_user.setText('')
                self.ui.Senha_verifica.setText('')
                self.ui.Senha_user.setFocus()

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
                        # TIME QUE ESTA VENCENDO NÃO SE MUDA
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
        self.ui = Ui_Tela_Principal()
        self.ui.setupUi(self)

        self.ui.Redireciona_loja.clicked.connect(self.redireciona_loja)
        self.ui.Abr_lista_amigos.clicked.connect(self.abr_lista_amigos)
        self.ui.Perfil_usuario.clicked.connect(self.perfil_usuario)
        self.ui.Ajuda.clicked.connect(self.ajuda)
        self.ui.AdicionarFundos.clicked.connect(self.adicionar_fundos)
        self.ui.Sair.clicked.connect(self.sair)
        self.ui.extra.clicked.connect(self.extra)

        # TABELA
        self.atualizar_tabela()
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.clicked.connect(self.botao_da_tabela)

        self.saldo_lcd = self.findChild(QtWidgets.QLCDNumber, 'Saldo')
        self.saldo_lcd.setDigitCount(10)

        # Defina o valor com a precisão desejada

        self.saldo_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.atualizar_saldo)


        self.timer.start(7000)
        self.valor = self.requisita_saldo()
        self.saldo_lcd.display(self.valor)

        print("------------------")
        print("Usuario ativo:", self.usuario_ativo)
        print("------------------")

        #TESTES COM THREADING
        # define o tempo para atualizar as threads
        t_atualiza_lista_jogos = threading.Timer(5.0, self.atualizar_tabela)
        #t_atualiza_saldo_usuario = threading.Timer(5.0, self.atualizar_tabela)
        # inicia as threads
        t_atualiza_lista_jogos.start()
        #t_atualiza_saldo_usuario.start()

        # aguarda as threads finalizarem


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
                print("Saldo recebido:", valor_saldo)
                return valor_saldo
        except Exception as erro:
            print(str(erro))

    def atualizar_saldo(self):

        novo_saldo = self.requisita_saldo()
        self.saldo_lcd.display(novo_saldo)
        print("Saldo da tabela:", novo_saldo)

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

    def extra(self):
        print("Login_admin")
        self.login_adm = Tela_login_adm()
        self.login_adm.show()
        # self.close() ERROR AQUI: RESOLVER PROBLEMA DE IMPORTAÇÃO CIRCULAR

    def redireciona_loja(self):
        print("Redireciona loja")
        pass

    def abr_lista_amigos(self):
        print("Abrir lista de amigos")
        pass

    def perfil_usuario(self):
        print("Perfil do usuario")
        pass

    def ajuda(self):
        print("Ajuda")
        self.tela_ajuda = Tela_adm_menu()
        self.tela_ajuda.show()


    def adicionar_fundos(self):
        print("Adicionar fundos")
        self.tela_adicionar_fundos = Tela_adicionar_fundos(usuario_ativo=self.usuario_ativo)
        self.tela_adicionar_fundos.show()
        self.requisita_saldo()


    def sair(self):
        self.close()
        self.tela_login_inst.show()


# 5 - Tela_adicionar_fundos
class Tela_adicionar_fundos(QMainWindow):
    def __init__(self, *args,usuario_ativo, **argvs):
        super(Tela_adicionar_fundos, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
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


# 7 - Tela_de_Ajuda
class Tela_adm_menu(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_adm_menu, self).__init__(*args, **argvs)
        self.ui = Ui_tela_ajuda()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.voltar)


    def voltar(self):
        print("Voltar")
        self.close()
