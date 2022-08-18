import MySQLdb

host = "localhost"
user = "aplicacao"
password = "senha"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)