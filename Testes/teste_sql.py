
import mysql.connector as mysql

conexao = mysql.connect(host = 'localhost', db = 'pooii', user = 'root', passwd = '20pmto4b')
cursor = conexao.cursor()

sql = """create table if not exists usuario_senha(id integer auto_increment primary key, usuario varchar(30) not null
, senha varchar(30), email varchar(30) not null)"""

nome = 'romuere'
senha = '123456'
email = 'romuere@email.com'

cursor.execute(sql)
cursor.execute("insert into usuario_senha(usuario, senha, email) values(%s, %s, %s)", (nome, senha, email))
conexao.commit()
cursor.close()
conexao.close()
