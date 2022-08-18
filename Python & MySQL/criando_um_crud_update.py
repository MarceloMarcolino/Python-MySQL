import MySQLdb

host = "localhost"
user = "aplicacao"
password = "senha"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):

	global c

	query = "SELECT " + fields + " FROM " + tables
	if (where):
		query = query + " WHERE " + where

	c.execute(query)
	return c.fetchall()

def insert(values, table, fields=None):

	global c, con

	query = "INSERT INTO " + table
	if (fields):
		query = query + " (" + fields + ") "
	query += " VALUES " + ",".join(["(" + v + ")" for v in values])

	c.execute(query)
	con.commit()

'''
UPDATE table
SET field = value, field = value
WHERE
'''

def update(sets, table, where=None):

	global c, con

	query = "UPDATE " + table
	query += " SET " + ",".join([field + " = '" + value +"'" for field, value in sets.items()])
	if (where):
		query += " WHERE " + where

	print(query)

	c.execute(query)
	con.commit()

print(select("*", "alunos", "id_aluno = 8"))
update({"nome":"João Martins","cidade":"Curitiba"}, "alunos", "id_aluno = 8")
print(select("*", "alunos", "id_aluno = 8"))