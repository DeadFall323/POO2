# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_adicionar_fundosbTUcIz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Qt import *

class Ui_adicionar_fundos(object):
    def setupUi(self, adicionar_fundos):
        if not adicionar_fundos.objectName():
            adicionar_fundos.setObjectName(u"adicionar_fundos")
        adicionar_fundos.resize(979, 624)
        adicionar_fundos.setStyleSheet(u"background-color: rgb(33, 35, 45);")
        self.centralwidget = QWidget(adicionar_fundos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
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
        self.frame_3.setMinimumSize(QSize(400, 0))
        self.frame_3.setStyleSheet(u"background-color:  rgb(68, 71, 90);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.adc_20 = QPushButton(self.frame_3)
        self.adc_20.setObjectName(u"adc_20")
        self.adc_20.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.adc_20)

        self.adc_50 = QPushButton(self.frame_3)
        self.adc_50.setObjectName(u"adc_50")
        self.adc_50.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.adc_50)

        self.adc_100 = QPushButton(self.frame_3)
        self.adc_100.setObjectName(u"adc_100")
        self.adc_100.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.adc_100)

        self.adc_200 = QPushButton(self.frame_3)
        self.adc_200.setObjectName(u"adc_200")
        self.adc_200.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.adc_200)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 497, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.cancelar = QPushButton(self.frame_4)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_3.addWidget(self.cancelar)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        adicionar_fundos.setCentralWidget(self.centralwidget)

        self.retranslateUi(adicionar_fundos)

        QMetaObject.connectSlotsByName(adicionar_fundos)
    # setupUi

    def retranslateUi(self, adicionar_fundos):
        adicionar_fundos.setWindowTitle(QCoreApplication.translate("adicionar_fundos", u"Adicionar Fundos", None))
        self.adc_20.setText(QCoreApplication.translate("adicionar_fundos", u"Adicionar R$ 20,00", None))
        self.adc_50.setText(QCoreApplication.translate("adicionar_fundos", u"Adicionar R$ 50,00", None))
        self.adc_100.setText(QCoreApplication.translate("adicionar_fundos", u"Adicionar R$ 100,00", None))
        self.adc_200.setText(QCoreApplication.translate("adicionar_fundos", u"Adicionar R$ 200,00", None))
        self.cancelar.setText(QCoreApplication.translate("adicionar_fundos", u"Voltar", None))
    # retranslateUi

