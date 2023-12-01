from PyQt5.QtWidgets import *

from Cliente.Modulos.Templates.Tela_ADM_Jogos import Ui_Tela_ADM_Menu
from Testes.adm.Tela_cadastrar_novo_jogo import Tela_inicial

class Tela_adm_menu(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_adm_menu, self).__init__(*args, **argvs)
        self.ui = Ui_Tela_ADM_Menu()
        self.ui.setupUi(self)

        self.ui.Cadastrar_jogo.clicked.connect(self.cadastrar_jogo)
        self.ui.Buscar_jogo.clicked.connect(self.buscar_jogo)
        self.ui.Remover_jogo.clicked.connect(self.remover_jogo)
        self.ui.Atualizar_jogo.clicked.connect(self.atualizar_jogo)
        self.ui.Buscar_Usuario.clicked.connect(self.buscar_Usuario)
        self.ui.Editar_usuario.clicked.connect(self.editar_usuario)
        self.ui.Verificar_jogos_usuario.clicked.connect(self.verificar_jogos_usuario)
        self.ui.sair.clicked.connect(self.Sair)

    def cadastrar_jogo(self):
        print("Cadastrar jogo")
        self.tela_cadastrar_jogo = Tela_inicial()
        self.tela_cadastrar_jogo.show()


    def buscar_jogo(self):
        print("Buscar jogo")
        pass

    def remover_jogo(self):
        print("Remover jogo")
        pass

    def atualizar_jogo(self):
        print("Atualizar jogo")
        pass

    def buscar_Usuario(self):
        print("Buscar Usuario")
        pass

    def editar_usuario(self):
        print("Editar usuario")
        pass

    def verificar_jogos_usuario(self):
        print("Verificar jogos do usuario")
        pass

    def Sair(self):
        self.close()

