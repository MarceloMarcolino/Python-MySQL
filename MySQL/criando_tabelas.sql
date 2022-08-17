#Tabela Alunos
#-Identificador de aluno (chave primária - tipo número)

#Tabela Cursos
#-Identificador de curso (chave primária - tipo número)

#Tabela Notas
#-Identificador de notas (chave primária - tipo número)

CREATE TABLE alunos (
  id_aluno INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_aluno)
);

CREATE TABLE cursos (
  id_curso INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_curso)
);

CREATE TABLE notas (
  id_nota INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_nota)
);