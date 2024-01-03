# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_principalYsLPwI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Qt import *

class Ui_Tela_principal(object):
    def setupUi(self, Tela_principal):
        if not Tela_principal.objectName():
            Tela_principal.setObjectName(u"Tela_principal")
        Tela_principal.resize(1180, 770)
        self.centralwidget = QWidget(Tela_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu_esquerdo = QFrame(self.frame)
        self.Menu_esquerdo.setObjectName(u"Menu_esquerdo")
        self.Menu_esquerdo.setMinimumSize(QSize(150, 0))
        self.Menu_esquerdo.setMaximumSize(QSize(50, 16777215))
        self.Menu_esquerdo.setStyleSheet(u"background-color:  rgb(68, 71, 90);")
        self.Menu_esquerdo.setFrameShape(QFrame.StyledPanel)
        self.Menu_esquerdo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Menu_esquerdo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.Menu_esquerdo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.Redireciona_loja = QPushButton(self.frame_2)
        self.Redireciona_loja.setObjectName(u"Redireciona_loja")
        self.Redireciona_loja.setMinimumSize(QSize(10, 0))
        self.Redireciona_loja.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.Redireciona_loja)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.Abr_lista_amigos = QPushButton(self.frame_2)
        self.Abr_lista_amigos.setObjectName(u"Abr_lista_amigos")
        self.Abr_lista_amigos.setStyleSheet(u"QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
" background-color: rgb(33, 35, 45);\n"
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

        self.verticalLayout_4.addWidget(self.Abr_lista_amigos)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.Perfil_usuario = QPushButton(self.frame_2)
        self.Perfil_usuario.setObjectName(u"Perfil_usuario")
        self.Perfil_usuario.setStyleSheet(u"QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
" background-color: rgb(33, 35, 45);\n"
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

        self.verticalLayout_4.addWidget(self.Perfil_usuario)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.configuracoes = QPushButton(self.frame_2)
        self.configuracoes.setObjectName(u"configuracoes")
        self.configuracoes.setMinimumSize(QSize(0, 0))
        self.configuracoes.setStyleSheet(u"QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
" background-color: rgb(33, 35, 45);\n"
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

        self.verticalLayout_4.addWidget(self.configuracoes, 0, Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.Menu_esquerdo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Sair = QPushButton(self.frame_3)
        self.Sair.setObjectName(u"Sair")
        self.Sair.setStyleSheet(u"QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(218, 218, 218);\n"
" background-color: rgb(33, 35, 45);\n"
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

        self.verticalLayout_5.addWidget(self.Sair)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.Menu_esquerdo)

        self.Menu_direito = QFrame(self.frame)
        self.Menu_direito.setObjectName(u"Menu_direito")
        self.Menu_direito.setStyleSheet(u"background-color: rgb(12, 10, 59);")
        self.Menu_direito.setFrameShape(QFrame.StyledPanel)
        self.Menu_direito.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Menu_direito)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Topo = QFrame(self.Menu_direito)
        self.Topo.setObjectName(u"Topo")
        self.Topo.setMinimumSize(QSize(50, 40))
        self.Topo.setStyleSheet(u"background-color: rgb(33, 35, 45);")
        self.Topo.setFrameShape(QFrame.StyledPanel)
        self.Topo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Topo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.Topo)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.exibenome = QLineEdit(self.frame_5)
        self.exibenome.setObjectName(u"exibenome")
        self.exibenome.setFrame(False)
        self.exibenome.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.exibenome)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.Topo)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.Topo)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(100, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Saldo = QLCDNumber(self.frame_8)
        self.Saldo.setObjectName(u"Saldo")
        self.Saldo.setMaximumSize(QSize(100, 40))
        self.Saldo.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Text Semibold\";")
        self.Saldo.setFrameShape(QFrame.VLine)
        self.Saldo.setFrameShadow(QFrame.Sunken)
        self.Saldo.setSmallDecimalPoint(False)
        self.Saldo.setDigitCount(6)
        self.Saldo.setProperty("value", 99999.000000000000000)

        self.verticalLayout_8.addWidget(self.Saldo)


        self.horizontalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.Topo)

        self.stackedWidget = QStackedWidget(self.Menu_direito)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.Loja = QWidget()
        self.Loja.setObjectName(u"Loja")
        self.horizontalLayout_4 = QHBoxLayout(self.Loja)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.tableWidget = QTableWidget(self.Loja)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.stackedWidget.addWidget(self.Loja)
        self.Perfil = QWidget()
        self.Perfil.setObjectName(u"Perfil")
        self.horizontalLayout_5 = QHBoxLayout(self.Perfil)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_7 = QFrame(self.Perfil)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.Perfil)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(200, 0))
        self.frame_9.setMaximumSize(QSize(300, 16777215))
        self.frame_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
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
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_8 = QLineEdit(self.frame_9)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_9.addWidget(self.lineEdit_8)

        self.lineEdit_7 = QLineEdit(self.frame_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_9.addWidget(self.lineEdit_7)

        self.lineEdit_6 = QLineEdit(self.frame_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_9.addWidget(self.lineEdit_6)


        self.horizontalLayout_5.addWidget(self.frame_9)

        self.Dados_usuario = QFrame(self.Perfil)
        self.Dados_usuario.setObjectName(u"Dados_usuario")
        self.Dados_usuario.setMinimumSize(QSize(200, 0))
        self.Dados_usuario.setMaximumSize(QSize(300, 16777215))
        self.Dados_usuario.setStyleSheet(u"color: rgb(255, 255, 255);\n"
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
        self.Dados_usuario.setFrameShape(QFrame.StyledPanel)
        self.Dados_usuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Dados_usuario)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lineEdit = QLineEdit(self.Dados_usuario)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_10.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.Dados_usuario)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_10.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.Dados_usuario)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_10.addWidget(self.lineEdit_3)


        self.horizontalLayout_5.addWidget(self.Dados_usuario)

        self.frame_11 = QFrame(self.Perfil)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.editar = QPushButton(self.frame_11)
        self.editar.setObjectName(u"editar")
        self.editar.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_12.addWidget(self.editar)

        self.adicionar_money = QPushButton(self.frame_11)
        self.adicionar_money.setObjectName(u"adicionar_money")
        self.adicionar_money.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_12.addWidget(self.adicionar_money)


        self.horizontalLayout_5.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.Perfil)
        self.Config = QWidget()
        self.Config.setObjectName(u"Config")
        self.label_5 = QLabel(self.Config)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(380, 220, 49, 16))
        self.stackedWidget.addWidget(self.Config)
        self.biblioteca = QWidget()
        self.biblioteca.setObjectName(u"biblioteca")
        self.label_6 = QLabel(self.biblioteca)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 300, 49, 16))
        self.stackedWidget.addWidget(self.biblioteca)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.Base = QFrame(self.Menu_direito)
        self.Base.setObjectName(u"Base")
        self.Base.setMinimumSize(QSize(30, 40))
        self.Base.setStyleSheet(u"background-color: rgb(33, 35, 45);")
        self.Base.setFrameShape(QFrame.StyledPanel)
        self.Base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Base)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.Base)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(111, 111, 111);")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.Base)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(111, 111, 111);")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.Base)


        self.horizontalLayout.addWidget(self.Menu_direito)


        self.verticalLayout.addWidget(self.frame)

        Tela_principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_principal)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Tela_principal)
    # setupUi

    def retranslateUi(self, Tela_principal):
        Tela_principal.setWindowTitle(QCoreApplication.translate("Tela_principal", u"Jogue Agora", None))
        self.label.setText(QCoreApplication.translate("Tela_principal", u"LOGO", None))
        self.Redireciona_loja.setText(QCoreApplication.translate("Tela_principal", u"LOJA", None))
        self.Abr_lista_amigos.setText(QCoreApplication.translate("Tela_principal", u"Biblioteca", None))
        self.Perfil_usuario.setText(QCoreApplication.translate("Tela_principal", u"PERFIL", None))
        self.configuracoes.setText(QCoreApplication.translate("Tela_principal", u"Config", None))
        self.Sair.setText(QCoreApplication.translate("Tela_principal", u"SAIR", None))
#if QT_CONFIG(whatsthis)
        self.Saldo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Tela_principal", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Tela_principal", u"Preco", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Tela_principal", u"Desenvolvedora", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Tela_principal", u"Preco", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Tela_principal", u"Desconto", None));
        self.label_4.setText(QCoreApplication.translate("Tela_principal", u"Foto", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Tela_principal", u"nome", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Tela_principal", u"email", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Tela_principal", u"nascimento", None))
        self.lineEdit.setText(QCoreApplication.translate("Tela_principal", u"Nome_usuario", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Tela_principal", u"telefone", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Tela_principal", u"rg", None))
        self.editar.setText(QCoreApplication.translate("Tela_principal", u"Editar", None))
        self.adicionar_money.setText(QCoreApplication.translate("Tela_principal", u"Adicionar Fundos", None))
        self.label_5.setText(QCoreApplication.translate("Tela_principal", u"Config", None))
        self.label_6.setText(QCoreApplication.translate("Tela_principal", u"biblioteca", None))
        self.label_2.setText(QCoreApplication.translate("Tela_principal", u"Desenvolvido por @Kawan", None))
        self.label_3.setText(QCoreApplication.translate("Tela_principal", u"Jogue Agora", None))
    # retranslateUi

