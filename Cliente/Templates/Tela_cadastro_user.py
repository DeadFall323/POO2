# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_login_cadastro2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Login_cadastro_user(object):
    def setupUi(self, Tela_Login_cadastro_user):
        Tela_Login_cadastro_user.setObjectName("Tela_Login_cadastro_user")
        Tela_Login_cadastro_user.resize(638, 493)
        self.centralwidget = QtWidgets.QWidget(Tela_Login_cadastro_user)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 622, 462))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Nome_completo = QtWidgets.QLineEdit(self.frame_3)
        self.Nome_completo.setGeometry(QtCore.QRect(10, 30, 281, 20))
        self.Nome_completo.setObjectName("Nome_completo")
        self.Endereco_email = QtWidgets.QLineEdit(self.frame_3)
        self.Endereco_email.setGeometry(QtCore.QRect(10, 100, 281, 20))
        self.Endereco_email.setObjectName("Endereco_email")
        self.Nome_usuario = QtWidgets.QLineEdit(self.frame_3)
        self.Nome_usuario.setGeometry(QtCore.QRect(10, 170, 281, 20))
        self.Nome_usuario.setObjectName("Nome_usuario")
        self.Telefone = QtWidgets.QLineEdit(self.frame_3)
        self.Telefone.setGeometry(QtCore.QRect(10, 240, 281, 20))
        self.Telefone.setObjectName("Telefone")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 201, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 201, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 201, 16))
        self.label_4.setObjectName("label_4")
        self.Voltar = QtWidgets.QPushButton(self.frame_3)
        self.Voltar.setGeometry(QtCore.QRect(10, 390, 241, 23))
        self.Voltar.setObjectName("Voltar")
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 201, 16))
        self.label_5.setObjectName("label_5")
        self.Senha_user = QtWidgets.QLineEdit(self.frame_2)
        self.Senha_user.setGeometry(QtCore.QRect(0, 30, 281, 20))
        self.Senha_user.setObjectName("Senha_user")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(0, 150, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(0, 80, 201, 16))
        self.label_8.setObjectName("label_8")
        self.Senha_verifica = QtWidgets.QLineEdit(self.frame_2)
        self.Senha_verifica.setGeometry(QtCore.QRect(0, 100, 281, 20))
        self.Senha_verifica.setObjectName("Senha_verifica")
        self.Nascimento = QtWidgets.QDateEdit(self.frame_2)
        self.Nascimento.setGeometry(QtCore.QRect(0, 170, 194, 22))
        self.Nascimento.setObjectName("Nascimento")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(0, 220, 201, 16))
        self.label_7.setObjectName("label_7")
        self.CPF = QtWidgets.QLineEdit(self.frame_2)
        self.CPF.setGeometry(QtCore.QRect(0, 240, 281, 20))
        self.CPF.setText("")
        self.CPF.setObjectName("CPF")
        self.Cadastrar_usuario = QtWidgets.QPushButton(self.frame_2)
        self.Cadastrar_usuario.setGeometry(QtCore.QRect(20, 390, 241, 23))
        self.Cadastrar_usuario.setObjectName("Cadastrar_usuario")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(30, 300, 215, 60))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_Termos = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_Termos.setObjectName("checkBox_Termos")
        self.verticalLayout.addWidget(self.checkBox_Termos)
        self.checkBox_notificadcoes = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_notificadcoes.setObjectName("checkBox_notificadcoes")
        self.verticalLayout.addWidget(self.checkBox_notificadcoes)
        self.horizontalLayout_2.addWidget(self.frame_2)
        Tela_Login_cadastro_user.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Login_cadastro_user)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        Tela_Login_cadastro_user.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Login_cadastro_user)
        self.statusbar.setObjectName("statusbar")
        Tela_Login_cadastro_user.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Login_cadastro_user)
        QtCore.QMetaObject.connectSlotsByName(Tela_Login_cadastro_user)

    def retranslateUi(self, Tela_Login_cadastro_user):
        _translate = QtCore.QCoreApplication.translate
        Tela_Login_cadastro_user.setWindowTitle(_translate("Tela_Login_cadastro_user", "MainWindow"))
        self.label.setText(_translate("Tela_Login_cadastro_user", "Nome Completo:"))
        self.label_2.setText(_translate("Tela_Login_cadastro_user", "Endereço de Email:"))
        self.label_3.setText(_translate("Tela_Login_cadastro_user", "Nome de Usuario:"))
        self.label_4.setText(_translate("Tela_Login_cadastro_user", "Telefone:"))
        self.Voltar.setText(_translate("Tela_Login_cadastro_user", "Cancelar"))
        self.label_5.setText(_translate("Tela_Login_cadastro_user", "Digite sua senha: "))
        self.label_6.setText(_translate("Tela_Login_cadastro_user", "Data de Nascimento:"))
        self.label_8.setText(_translate("Tela_Login_cadastro_user", "Digite a senha Novamente:"))
        self.label_7.setText(_translate("Tela_Login_cadastro_user", "CPF:"))
        self.Cadastrar_usuario.setText(_translate("Tela_Login_cadastro_user", "Cadastrar"))
        self.checkBox_Termos.setText(_translate("Tela_Login_cadastro_user", "Aceite os Termos"))
        self.checkBox_notificadcoes.setText(_translate("Tela_Login_cadastro_user", "Receber notificações sobre ofertas."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Login_cadastro_user = QtWidgets.QMainWindow()
    ui = Ui_Tela_Login_cadastro_user()
    ui.setupUi(Tela_Login_cadastro_user)
    Tela_Login_cadastro_user.show()
    sys.exit(app.exec_())
