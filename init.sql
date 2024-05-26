/*Drop all Tables*/
DROP TABLE IF EXISTS clinica CASCADE;
DROP TABLE IF EXISTS enfermeiro CASCADE;
DROP TABLE IF EXISTS medico CASCADE;
DROP TABLE IF EXISTS trabalha CASCADE;
DROP TABLE IF EXISTS paciente CASCADE;
DROP TABLE IF EXISTS receita CASCADE;
DROP TABLE IF EXISTS consulta CASCADE;
DROP TABLE IF EXISTS observacao CASCADE;

/*Create Table Clínica*/
CREATE TABLE clinica(
nome VARCHAR(80) PRIMARY KEY,
telefone VARCHAR(15) UNIQUE NOT NULL CHECK (telefone ~ '^[0-9]+$'),
morada VARCHAR(255) UNIQUE NOT NULL
);

/*Create Table Enfermeiro*/
CREATE TABLE enfermeiro(
nif CHAR(9) PRIMARY KEY CHECK (nif ~ '^[0-9]+$'),
nome VARCHAR(80) UNIQUE NOT NULL,
telefone VARCHAR(15) NOT NULL CHECK (telefone ~ '^[0-9]+$'),
morada VARCHAR(255) NOT NULL,
nome_clinica VARCHAR(80) NOT NULL REFERENCES clinica (nome)
);

/*Create Table Médico*/
CREATE TABLE medico(
nif CHAR(9) PRIMARY KEY CHECK (nif ~ '^[0-9]+$'),
nome VARCHAR(80) UNIQUE NOT NULL,
telefone VARCHAR(15) NOT NULL CHECK (telefone ~ '^[0-9]+$'),
morada VARCHAR(255) NOT NULL,
especialidade VARCHAR(80) NOT NULL
);

/*Create Table Trabalha*/
CREATE TABLE trabalha(
nif CHAR(9) NOT NULL REFERENCES medico,
nome VARCHAR(80) NOT NULL REFERENCES clinica,
dia_da_semana SMALLINT,
PRIMARY KEY (nif, dia_da_semana)
);

/*Create Table Paciente*/
CREATE TABLE paciente(
ssn CHAR(11) PRIMARY KEY CHECK (ssn ~ '^[0-9]+$'),
nif CHAR(9) UNIQUE NOT NULL CHECK (nif ~ '^[0-9]+$'),
nome VARCHAR(80) NOT NULL,
telefone VARCHAR(15) NOT NULL CHECK (telefone ~ '^[0-9]+$'),
morada VARCHAR(255) NOT NULL,
data_nasc DATE NOT NULL
);

/*Create Table Consulta*/
CREATE TABLE consulta(
id SERIAL PRIMARY KEY,
ssn CHAR(11) NOT NULL REFERENCES paciente,
nif CHAR(9) NOT NULL REFERENCES medico,
nome VARCHAR(80) NOT NULL REFERENCES clinica,
data DATE NOT NULL,
hora TIME NOT NULL,
codigo_sns CHAR(12) UNIQUE CHECK (codigo_sns ~ '^[0-9]+$'),
UNIQUE(ssn, data, hora),
UNIQUE(nif, data, hora),

/*Implement integrity restriction for the time of the consultation -> RI-1*/
CHECK (
        (EXTRACT(HOUR FROM hora) BETWEEN 8 AND 12 OR EXTRACT(HOUR FROM hora) BETWEEN 14 AND 19)
        AND
        ((EXTRACT(HOUR FROM hora) * 60 + EXTRACT(MINUTE FROM hora)) % 30 = 0)
    )
);

/*Create Table Receita*/
CREATE TABLE receita(
codigo_sns VARCHAR(12) NOT NULL REFERENCES consulta (codigo_sns),
medicamento VARCHAR(155) NOT NULL,
quantidade SMALLINT NOT NULL CHECK (quantidade > 0),
PRIMARY KEY (codigo_sns, medicamento)
);

/*Create Table Observação*/
CREATE TABLE observacao(
id INTEGER NOT NULL REFERENCES consulta,
parametro VARCHAR(155) NOT NULL,
valor FLOAT,
PRIMARY KEY (id, parametro)
);

/*TRIGGER to prevent an insertion in consulta where a medico consults themselves -> RI-2*/
CREATE OR REPLACE FUNCTION check_medico_consulta_self_func() RETURNS TRIGGER AS 
$$
DECLARE
nif_paciente CHAR(9);
BEGIN 
    /*Get the NIF of the patient to be consulted, through the SSN in the new entry of consulta*/
    SELECT nif INTO nif_paciente FROM paciente WHERE ssn = NEW.ssn;
    IF NEW.nif = nif_paciente THEN
        RAISE EXCEPTION 'O médico não se pode consultar a si mesmo: NIF: %', NEW.nif;
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

/*Create the TRIGGER*/
CREATE TRIGGER check_medico_consulta_self
BEFORE INSERT ON consulta
FOR EACH ROW
EXECUTE FUNCTION check_medico_consulta_self_func();

/*TRIGGER to prevent an insertion in consulta where a medico is not working in the given clinica at the specified date -> RI-3*/
CREATE OR REPLACE FUNCTION check_medico_in_clinica_func() RETURNS TRIGGER AS
$$
DECLARE appointement_week_day SMALLINT;
BEGIN
    /*Get the day of the week of the date of the appointment*/
    appointement_week_day := EXTRACT(DOW FROM NEW.data);
    /*Check if the medico is working in the clinica at the given day of the week*/
    IF NEW.nome NOT IN (SELECT nome FROM trabalha WHERE nif = NEW.nif AND dia_da_semana = appointement_week_day) THEN
        RAISE EXCEPTION 'O médico não trabalha na clínica na data da consulta: NIF: %, Clínica: %, Data: %, Dia da semana: %', NEW.nif, NEW.nome, NEW.data, appointement_week_day;
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

/*Create the TRIGGER*/
CREATE OR REPLACE TRIGGER check_medico_in_clinica
BEFORE INSERT ON consulta
FOR EACH ROW
EXECUTE FUNCTION check_medico_in_clinica_func();






