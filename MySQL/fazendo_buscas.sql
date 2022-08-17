SELECT *
FROM alunos;

SELECT cidade, data_nascimento, cpf
FROM alunos;

SELECT nome, cidade, data_nascimento, cpf
FROM alunos
WHERE cidade = 'BELO HORIZONTE';

SELECT *
FROM alunos
ORDER BY nome;

SELECT *
FROM alunos
ORDER BY cidade;

SELECT *
FROM alunos
ORDER BY nome DESC;

SELECT nome, data_nascimento, endereco
FROM alunos
ORDER BY 2 DESC;