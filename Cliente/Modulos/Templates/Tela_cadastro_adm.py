# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_cadastro_adm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cadastro_adm(object):
    def setupUi(self, Cadastro_adm):
        Cadastro_adm.setObjectName("Cadastro_adm")
        Cadastro_adm.resize(755, 586)
        self.centralwidget = QtWidgets.QWidget(Cadastro_adm)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("/* Aplicando o estilo antigo com tons de cinza */\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(218, 218, 218);\n"
"background-color: rgb(60, 60, 60);\n"
"border: none; /* Removendo o contorno das bordas nos quadros */\n"
"border-radius: 3px;\n"
"padding: 8px 16px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setMinimumSize(QtCore.QSize(340, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setStyleSheet("    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_3.setStyleSheet("    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_7.addWidget(self.lineEdit_3)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 88, 88); /* Cor de fundo quando o botão é destacado */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 40, 40); /* Cor de fundo quando o botão é pressionado */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_10.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setStyleSheet("    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_4.setStyleSheet("    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_8.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self.frame_11)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 88, 88); /* Cor de fundo quando o botão é destacado */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 40, 40); /* Cor de fundo quando o botão é pressionado */\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_11)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        Cadastro_adm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Cadastro_adm)
        self.statusbar.setObjectName("statusbar")
        Cadastro_adm.setStatusBar(self.statusbar)

        self.retranslateUi(Cadastro_adm)
        QtCore.QMetaObject.connectSlotsByName(Cadastro_adm)

    def retranslateUi(self, Cadastro_adm):
        _translate = QtCore.QCoreApplication.translate
        Cadastro_adm.setWindowTitle(_translate("Cadastro_adm", "Cadastrar_adm"))
        self.label.setText(_translate("Cadastro_adm", "Cadastre um Novo Administrador"))
        self.label_2.setText(_translate("Cadastro_adm", "Insira o nome:"))
        self.label_4.setText(_translate("Cadastro_adm", "Insira o sobrenome:"))
        self.pushButton_2.setText(_translate("Cadastro_adm", "Cancelar"))
        self.label_3.setText(_translate("Cadastro_adm", "Insira a senha:"))
        self.label_5.setText(_translate("Cadastro_adm", "Insira a senha novamente:"))
        self.pushButton.setText(_translate("Cadastro_adm", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro_adm = QtWidgets.QMainWindow()
    ui = Ui_Cadastro_adm()
    ui.setupUi(Cadastro_adm)
    Cadastro_adm.show()
    sys.exit(app.exec_())