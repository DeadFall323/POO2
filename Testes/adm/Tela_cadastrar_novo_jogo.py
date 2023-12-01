from PyQt5.QtWidgets import *

import mysql.connector as mysql
import traceback

from Cliente.Modulos.Templates.Tela_cad_novo_jogo import Ui_MainWindow

class Tela_inicial(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Tela_inicial, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cadastrar.clicked.connect(self.cadastrar)
        self.ui.cancelar.clicked.connect(self.cancelar)

    def cancelar(self):
        self.close()

    def cadastrar(self):
        nome_jogo = self.ui.Nome_jogo.text()
        desenvolvedora = self.ui.Desenvolvedor.text()
        distribuidora = self.ui.Distribuidor.text()
        requisitos_CPU = self.ui.RE_CPU.text()
        requisitos_GPU = self.ui.RE_GPU.text()
        requisitos_memoria = self.ui.RE_Memoria.text()
        requisitos_armazenamento = self.ui.RE_armazenamento.text()
        requisitos_outros = self.ui.RE_Outros.text()
        genero = self.ui.Genero.text()
        requisitos_sistema = self.ui.RE_Sistema.text()

        preco = float(self.ui.Preco.text())
        desconto = float(self.ui.Desconto.text())

        if nome_jogo == "" or desenvolvedora == "" or distribuidora == "" or requisitos_CPU == "" or requisitos_GPU == "" or requisitos_memoria == "" or requisitos_armazenamento == "" or requisitos_outros == "" or genero == "" or requisitos_sistema == "":
            QMessageBox.about(self, "Erro", "Preencha todos os campos")
        else:
            try:
                conn = mysql.connect(
                    host='localhost',
                    database='pooii',
                    user='root',
                    password='20pmto4b'
                )
                cursor = conn.cursor()

                query = """INSERT INTO jogos 
                           (nome_jogo, desenvolvedor, distribuidor, requisitos_cpu, requisitos_gpu, requisitos_memoria, 
                           armazenamento, requisitos_outros, jogo_genero, requisitos_so, preco, desconto) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                data = (nome_jogo, desenvolvedora, distribuidora, requisitos_CPU, requisitos_GPU, requisitos_memoria,
                        requisitos_armazenamento, requisitos_outros, genero, requisitos_sistema, preco, desconto)

                cursor.execute(query, data)
                conn.commit()
                conn.close()

                QMessageBox.about(self, "Sucesso", "Jogo cadastrado com sucesso")
                self.close()
            except mysql.Error as e:
                QMessageBox.about(self, "Erro", f"Erro ao cadastrar jogo: {str(e)}")
                print(traceback.format_exc())
                self.close()


