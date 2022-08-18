import MySQLdb

host = "localhost"
user = "aplicacao"
password = "senha"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor()

def select(fields, tables, where=None):

	global c

	query = "SELECT " + fields + " FROM " + tables
	if (where):
		query = query + " WHERE " + where

	c.execute(query)
	return c.fetchall()

print(select("nome, cpf","alunos","id_aluno = 1"))

result = select("nome, cpf","alunos")
print(result)
print(result[0])
print(result[0][0])

c = con.cursor(MySQLdb.cursors.DictCursor)
result = select("nome, cpf","alunos")
print(result)
print(result[0]["nome"])
print(result[0]["cpf"])