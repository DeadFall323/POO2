from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os
import sys
from Raiz import Tela_login
import socket


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Tela_login()
    login_window.show()
    sys.exit(app.exec_())