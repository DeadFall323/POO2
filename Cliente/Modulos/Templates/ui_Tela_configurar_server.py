# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_configurar_serverbgxyqV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Qt import *


class Ui_Tela_configurar_server(object):
    def setupUi(self, Tela_configurar_server):
        if not Tela_configurar_server.objectName():
            Tela_configurar_server.setObjectName(u"Tela_configurar_server")
        Tela_configurar_server.resize(918, 536)
        Tela_configurar_server.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(Tela_configurar_server)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_2)

        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setStyleSheet(u"background-color:  rgb(68, 71, 90);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Segoe UI\";\n"
"QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #32314f; /* Cor da borda */\n"
"    border-radius: 5px; /* Valor para arredondar os cantos */\n"
"    background-color: #ffffff; /* Cor de fundo */\n"
"    color: #32314f; /* Cor do texto */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(62, 52, 84); /* Cor da borda quando em foco */\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(33, 35, 45);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 88, 88); /* Cor de fundo quando o bot\u00e3o \u00e9 destacado */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 40, 40); /* Cor de fundo quando o bot\u00e3o \u00e9 pressionado */\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"\n"
"QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #32314f; /* Cor da borda */\n"
"    border-radius: 5px; /* Valor para arredondar os cantos */\n"
"    background-color: #ffffff; /* Cor de fundo */\n"
"    color: #32314f; /* Cor do texto */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(62, 52, 84); /* Cor da borda quando em foco */\n"
"}")

        self.verticalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.frame_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"\n"
"QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #32314f; /* Cor da borda */\n"
"    border-radius: 5px; /* Valor para arredondar os cantos */\n"
"    background-color: #ffffff; /* Cor de fundo */\n"
"    color: #32314f; /* Cor do texto */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(62, 52, 84); /* Cor da borda quando em foco */\n"
"}")

        self.verticalLayout_7.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(33, 35, 45);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 88, 88); /* Cor de fundo quando o bot\u00e3o \u00e9 destacado */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 40, 40); /* Cor de fundo quando o bot\u00e3o \u00e9 pressionado */\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color:  rgb(68, 71, 90);\n"
"font: 9pt \"Segoe UI Symbol\";\n"
"color: rgb(0, 0, 0);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.checkBox = QCheckBox(self.frame_9)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)

        self.verticalLayout_5.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_9)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBox_2)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgb(33, 35, 45);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 88, 88); /* Cor de fundo quando o bot\u00e3o \u00e9 destacado */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 40, 40); /* Cor de fundo quando o bot\u00e3o \u00e9 pressionado */\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        Tela_configurar_server.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_configurar_server)

        QMetaObject.connectSlotsByName(Tela_configurar_server)
    # setupUi

    def retranslateUi(self, Tela_configurar_server):
        Tela_configurar_server.setWindowTitle(QCoreApplication.translate("Tela_configurar_server", u"Jogue Agora", None))
        self.label_2.setText(QCoreApplication.translate("Tela_configurar_server", u"Aten\u00e7\u00e3o: utilize o Ip e Porta especificados no servidor", None))
        self.label_5.setText(QCoreApplication.translate("Tela_configurar_server", u"Depois aperte em verificar", None))
        self.label_3.setText(QCoreApplication.translate("Tela_configurar_server", u"IP:", None))
        self.label_4.setText(QCoreApplication.translate("Tela_configurar_server", u"Porta", None))
        self.pushButton.setText(QCoreApplication.translate("Tela_configurar_server", u"Verificar", None))
        self.label.setText(QCoreApplication.translate("Tela_configurar_server", u"Conex\u00f5es do aplicativo", None))
        self.checkBox.setText(QCoreApplication.translate("Tela_configurar_server", u"Server", None))
        self.checkBox_2.setText(QCoreApplication.translate("Tela_configurar_server", u"Banco de Dados", None))
        self.pushButton_3.setText(QCoreApplication.translate("Tela_configurar_server", u"Sair", None))
    # retranslateUi

