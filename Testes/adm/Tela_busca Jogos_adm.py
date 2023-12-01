from PyQt5.QtWidgets import *

from Cliente.Modulos.Templates.Tela_buscar_jogos_adm import Ui_Buscar_jogo

class Tela_login(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_login, self).__init__(*args, **argvs)
        self.ui = Ui_Buscar_jogo()
        self.ui.setupUi(self)




