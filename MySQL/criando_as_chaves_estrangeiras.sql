/*Tabela Alunos Cursos
Identificador de alunos e cursos (chave primária - tipo número)
Identificador de alunos (chave estrangeira - tipo número)
Identificador de cursos (chave estrangeira - tipo número)

Tabela Notas
Identificador de notas (chave primária - tipo número)
Identificador de alunos e cursos (chave estrangeira - tipo número)*/

ALTER TABLE `escola_curso`.`alunos_cursos` 
ADD INDEX `fk_id_aluno_idx` (`id_aluno` ASC) VISIBLE,
ADD INDEX `fk_id_curso_idx` (`id_curso` ASC) VISIBLE;
;
ALTER TABLE `escola_curso`.`alunos_cursos` 
ADD CONSTRAINT `fk_id_aluno`
  FOREIGN KEY (`id_aluno`)
  REFERENCES `escola_curso`.`alunos` (`id_aluno`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_id_curso`
  FOREIGN KEY (`id_curso`)
  REFERENCES `escola_curso`.`cursos` (`id_curso`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
ALTER TABLE `escola_curso`.`notas` 
ADD COLUMN `id_aluno_curso` INT NOT NULL AFTER `id_nota`,
ADD INDEX `fk_id_aluno_curso_idx` (`id_aluno_curso` ASC) VISIBLE;
;
ALTER TABLE `escola_curso`.`notas` 
ADD CONSTRAINT `fk_id_aluno_curso`
  FOREIGN KEY (`id_aluno_curso`)
  REFERENCES `escola_curso`.`alunos_cursos` (`id_aluno_curso`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
