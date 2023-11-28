from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os
import sys
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from Cliente.Templates.Tela_buscar_jogos_adm import Ui_Buscar_jogo

class Tela_login(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_login, self).__init__(*args, **argvs)
        self.ui = Ui_Buscar_jogo()
        self.ui.setupUi(self)




