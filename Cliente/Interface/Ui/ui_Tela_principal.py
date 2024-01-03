# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_principalNVfKxd.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1005, 705)
        self.centralwidget = QWidget(MainWindow)
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
        self.Menu_esquerdo.setMinimumSize(QSize(100, 0))
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
        self.verticalLayout_9 = QVBoxLayout(self.Loja)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tableWidget = QTableWidget(self.Loja)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_9.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.Loja)
        self.Perfil = QWidget()
        self.Perfil.setObjectName(u"Perfil")
        self.stackedWidget.addWidget(self.Perfil)
        self.Config = QWidget()
        self.Config.setObjectName(u"Config")
        self.stackedWidget.addWidget(self.Config)
        self.Amigos = QWidget()
        self.Amigos.setObjectName(u"Amigos")
        self.stackedWidget.addWidget(self.Amigos)

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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jogue Agora", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.Redireciona_loja.setText(QCoreApplication.translate("MainWindow", u"LOJA", None))
        self.Abr_lista_amigos.setText(QCoreApplication.translate("MainWindow", u"Amigos", None))
        self.Perfil_usuario.setText(QCoreApplication.translate("MainWindow", u"PERFIL", None))
        self.configuracoes.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.Sair.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
#if QT_CONFIG(whatsthis)
        self.Saldo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Preco", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por @Kawan", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Jogue Agora", None))
    # retranslateUi

