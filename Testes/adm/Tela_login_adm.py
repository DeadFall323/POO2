from PyQt5.QtWidgets import *
import mysql.connector as mysql

from Cliente.Modulos.Templates.Tela_Login_adm import Ui_Login_ADM
from Testes.adm.Tela_ADM_jogos import Tela_adm_menu
from Testes.adm.Tela_cadastro_adm import Tela_inicial


class Login_adm(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Login_adm, self).__init__(*args, **argvs)
        self.ui = Ui_Login_ADM()
        self.ui.setupUi(self)

        self.ui.Login.clicked.connect(self.login)
        self.ui.Voltar.clicked.connect(self.voltar)
        self.ui.pushButton_3.clicked.connect(self.cadastrar)

    def cadastrar(self):
        print("Cadastrar")
        self.window = Tela_inicial()
        self.window.show()

    def login(self):
        print("Login")

        emailadm = "adm"
        senhaadm = "adm"

        conexao = mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b')
        cursor = conexao.cursor()

        usuario = self.ui.Usuario_ADM.text()
        senha = self.ui.Senha_adm.text()

        print("Email:", usuario)
        print("Senha:", senha)

        cursor.execute("SELECT * FROM administradores WHERE Nome_adm = %s AND senha_adm = %s", (usuario, senha))
        resultado = cursor.fetchone()
        conexao.close()

        if usuario == emailadm and senha == senhaadm:
            # QMessageBox.about(self, "Login", "Login realizado com sucesso!")
            self.window = Tela_adm_menu()
            self.window.show()
            self.close()

        if resultado:
            # QMessageBox.about(self, "Login", "Login realizado com sucesso!")
            self.window = Tela_adm_menu()
            self.window.show()
            self.close()

        else:
            QMessageBox.about(self, "Login", "Usuario ou Senha Inválidos!")
            self.ui.Usuario_ADM.setText('')
            self.ui.Senha_adm.setText('')
            self.ui.Usuario_ADM.setFocus()

    def voltar(self):
        print("Voltar")
        self.close()

