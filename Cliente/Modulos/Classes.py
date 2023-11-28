class Usuario:
    def __init__(self,nome, email, nome_usuario, telefone, senha, conf_senha, nascimento, rg, saldo, id_usuario):
        self.nome = nome
        self.email = email
        self.nome_usuario = nome_usuario
        self.telefone = telefone
        self.senha = senha
        self.conf_senha = conf_senha
        self.nascimento = nascimento
        self.rg = rg
        self.saldo = saldo
        self.id_usuario = id_usuario


class Sessao:
    def __init__(self, nome, id_usuario, email, nome_usuario, telefone, senha, nascimento, rg, saldo):
        self.nome = nome
        self.id_usuario = id_usuario
        self.email = email
        self.nome_usuario = nome_usuario
        self.telefone = telefone
        self.senha = senha
        self.nascimento = nascimento
        self.rg = rg
        self.saldo = saldo



    def separa_sessao(self, dados_servidor):

        sessao = ast.literal_eval(dados_servidor)

        if len(dados_servidor) >= 7:
            Nome, Nome_usuario, Telefone, data_nascimento, RG, Saldo, email = sessao[:7]


            """print("Nome:", Nome)
            print("Nome_usuario:", Nome_usuario)
            print("Telefone:", Telefone)
            print("Data de nascimento:", data_nascimento)
            print("RG:", RG)
            print("Saldo:", Saldo)
            print("E-mail:", email)"""
            return email
        else:
            print("A tupla não contém sete valores.")

    def requisita_sessao(self):
        addr = conecta_servidor()
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(addr)

            while True:
                operacao = 'requisita_sessao'
                msg1 = "ignore_requisita_sessao2"
                msg2 = 'ignore_requisita_sessao2'
                comando = operacao + "," + msg1 + "," + msg2
                client_socket.send(comando.encode('utf-8'))

                recebe = client_socket.recv(1024)
                sessao = recebe.decode('utf-8')
                print("Sessao recebida:", sessao)

                return sessao

        except Exception as erro:
            print(str(erro))

