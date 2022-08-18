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

	#INSERT INTO <table> (fields) VALUES (),(),()

	query = "INSERT INTO " + table
	if (fields):
		query = query + " (" + fields + ") "
	query += " VALUES " + ",".join(["(" + v + ")" for v in values])

	c.execute(query)
	con.commit()

values = [
	"DEFAULT,'João Pedro', '2000-01-01', 'Av das Pedras, 123', 'Betim', 'MG', '12345678912'",
	"DEFAULT,'Maria Pedro', '2000-01-01', 'Av das Pedras, 123', 'Betim', 'MG', '12345678910'"]

insert(values, "alunos")
print(select("*","alunos"))