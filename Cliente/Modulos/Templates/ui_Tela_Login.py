# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_LoginphUBKi.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Qt import *


class Ui_tela_login(object):
    def setupUi(self, tela_login):
        if tela_login.objectName():
            tela_login.setObjectName(u"tela_login")
        tela_login.resize(908, 703)
        tela_login.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(tela_login)
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

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(350, 0))
        self.frame_3.setMaximumSize(QSize(350, 900))
        self.frame_3.setStyleSheet(u"background-color:  rgb(68, 71, 90);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton {\n"
"	font: 12pt \"Segoe UI\";\n"
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
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Segoe UI\";\n"
"")

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
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

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 300))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
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
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.lineEdit_2)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 80))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    padding: 5px 10px;\n"
"    font: 16pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 10px; /* Valor para arredondar os cantos */\n"
"    background-color: #32314f; /* Cor de fundo desejada */\n"
"    color: #ffffff; /* Cor do texto */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 52, 84); /* Roxo suave no hover */\n"
"    color: #ffffff; /* Branco no hover */\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 40))
        self.pushButton_2.setMaximumSize(QSize(190, 40))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    padding: 5px 10px;\n"
"    font: 16pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 10px; /* Valor para arredondar os cantos */\n"
"    background-color: #32314f; /* Cor de fundo desejada */\n"
"    color: #ffffff; /* Cor do texto */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 52, 84); /* Roxo suave no hover */\n"
"    color: #ffffff; /* Branco no hover */\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        tela_login.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_login)

        QMetaObject.connectSlotsByName(tela_login)
    # setupUi

    def retranslateUi(self, tela_login):
        tela_login.setWindowTitle(QCoreApplication.translate("tela_login", u"Jogue Agora", None))
        self.label_2.setText(QCoreApplication.translate("tela_login", u"Email:", None))
        self.label_3.setText(QCoreApplication.translate("tela_login", u"Senha:", None))
        self.pushButton.setText(QCoreApplication.translate("tela_login", u"Esqueceu a senha?", None))
        self.pushButton_2.setText(QCoreApplication.translate("tela_login", u"Login", None))
        self.pushButton_3.setText(QCoreApplication.translate("tela_login", u"Sair", None))
    # retranslateUi

