from PyQt5.QtWidgets import *
import mysql.connector as mysql

from Cliente.Modulos.Templates.Tela_cadastro_adm import Ui_Cadastro_adm

class Tela_inicial(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_inicial, self).__init__(*args, **argvs)
        self.ui = Ui_Cadastro_adm()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.cadastrar)
        self.ui.pushButton_2.clicked.connect(self.voltar)

    def cadastrar(self):
        print("Cadastrar")

        nome = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()
        sobrenome = self.ui.lineEdit_3.text()
        conf_senha = self.ui.lineEdit_4.text()

        if senha == conf_senha:
            if nome == '' or sobrenome == '' or senha == '' or conf_senha == '':
                QMessageBox.about(self, "Cadastro", "Preencha todos os campos!")
            else:
                self.ui.lineEdit.setText('')
                self.ui.lineEdit_2.setText('')
                self.ui.lineEdit_3.setText('')
                self.ui.lineEdit_4.setText('')

                try:
                    conn = mysql.connect(host='localhost', db='pooii', user='root', passwd='20pmto4b')
                    cursor = conn.cursor()
                    cursor.execute("""insert into administradores(Nome_adm, sobrenome_adm, senha_adm) values(%s, %s, %s)""",
                                   (nome, sobrenome, senha))

                    conn.commit()
                    conn.close()

                    QMessageBox.about(self, "Cadastro", "Cadastro realizado com sucesso!")

                except:

                    QMessageBox.about(self, "Cadastro", "Erro ao cadastrar!")


                print("Cadastro realizado com sucesso!")
                self.close()
        else:
            QMessageBox.about(self, "Cadastro", "Senhas não coincidem!")
            self.ui.lineEdit_3.setText('')
            self.ui.lineEdit_4.setText('')
            self.ui.lineEdit_3.setFocus()


    def voltar(self):
        print("Voltar")
        pass

