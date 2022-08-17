SELECT *
FROM alunos
WHERE id_aluno = 2 or id_aluno = 5;

SELECT *
FROM alunos
WHERE cidade = 'BELO HORIZONTE' and estado = 'MG';

SELECT *
FROM alunos
WHERE data_nascimento > '1990-01-01';

SELECT *
FROM alunos
WHERE data_nascimento >= '1990-01-01';

SELECT *
FROM alunos
WHERE data_nascimento <> '1990-01-01';


/*
>=
<=
=
<>, equivale à diferente
*/