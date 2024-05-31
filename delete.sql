-- Delete all data from the existing tables
BEGIN;

-- Delete all data from table observacao
DELETE FROM observacao;

-- Delete all data from table receita
DELETE FROM receita;

-- Delete all data from table consulta
DELETE FROM consulta;

-- Delete all data from table paciente
DELETE FROM paciente;

-- Delete all data from table trabalha
DELETE FROM trabalha;

-- Delete all data from table medico
DELETE FROM medico;

-- Delete all data from table enfermeiro
DELETE FROM enfermeiro;

-- Delete all data from table clinica
DELETE FROM clinica;

END;



