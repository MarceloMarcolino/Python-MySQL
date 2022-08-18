INSERT INTO cursos
VALUES
(DEFAULT, "Codeigniter"),
(DEFAULT, "Python"),
(DEFAULT, "MySQL");

INSERT INTO alunos_cursos
VALUES
(DEFAULT, 1, 1), -- 1
(DEFAULT, 1, 2), -- 2
(DEFAULT, 2, 1), -- 3
(DEFAULT, 2, 3), -- 4
(DEFAULT, 3, 1), -- 5
(DEFAULT, 3, 2), -- 6
(DEFAULT, 4, 1), -- 7
(DEFAULT, 5, 1); -- 8

INSERT INTO notas
VALUES
(DEFAULT, 1, 'Prova 1', 28.0), # Pedro fez a atividade Prova 1 no Codeigniter e tirou 28.0
(DEFAULT, 1, 'Prova 2', 25.0), # Pedro fez a atividade Prova 2 no Codeigniter e tirou 25.0
(DEFAULT, 2, 'Prova 2', 20.0), # Pedro fez a atividade Prova 2 no Python e tirou 20.0
(DEFAULT, 2, 'Exercicio 2', 10.0), # Pedro fez a atividade Exercício 2 no Python e tirou 10.0
(DEFAULT, 3, 'Prova 1', 25.0), # Diego fez a atividade Prova 1 no Codeigniter e tirou 25.0
(DEFAULT, 5, 'Prova 1', 28.0), # Fliper fez a atividade Prova 1 no Codeigniter e tirou 28.0
(DEFAULT, 6, 'Exercicio 2', 12.0); # Fliper fez a atividade Exercicio 2 no Python e tirou 12.0

SELECT * FROM alunos;
SELECT * FROM alunos_cursos;
SELECT * FROM cursos;
SELECT * FROM notas;

SELECT A.nome, AC.id_curso
FROM alunos A, alunos_cursos AC
WHERE A.id_aluno = AC.id_aluno;

SELECT A.id_aluno, A.nome, C.id_curso, C.nome
FROM alunos A,
	cursos C,
	alunos_cursos AC
WHERE A.id_aluno = AC.id_aluno and C.id_curso = AC.id_curso;

SELECT A.nome, C.nome, N.descricao_atividade, N.vlr_nota
FROM alunos A,
	cursos C,
	alunos_cursos AC,
    notas N
WHERE A.id_aluno = AC.id_aluno and C.id_curso = AC.id_curso and AC.id_aluno_curso = N.id_aluno_curso;