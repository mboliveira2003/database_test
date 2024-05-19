/*Populate clinica*/
INSERT INTO clinica (nome, telefone, morada) VALUES
('Clinica São João', '963456789', 'Rua das Flores, 1234 Lisboa 1000-001'),
('Clinica Esperança', '987654321', 'Avenida Central, 567 Cascais 2765-001'),
('Clinica Saúde Feliz', '911222333', 'Travessa das Oliveiras, 89 Sintra 2710-001'),
('Clinica Bem-Estar', '934555666', 'Praça da Liberdade, 10 Oeiras 2780-001'),
('Clinica Harmonia', '947888999', 'Estrada Principal, 45 Amadora 2650-001');

/*Populate enfermeiro*/
INSERT INTO enfermeiro (nif, nome, telefone, morada, nome_clinica) VALUES
('123456789', 'Ana Silva', '911111111', 'Rua dos Enfermeiros, 1 Lisboa 1000-001', 'Clinica São João'),
('234567890', 'Pedro Santos', '922222222', 'Avenida dos Cuidados, 2 Lisboa 1000-001', 'Clinica São João'),
('345678901', 'Marta Oliveira', '933333333', 'Travessa dos Cuidados, 3 Lisboa 1000-001', 'Clinica São João'),
('456789012', 'Rita Ferreira', '944444444', 'Praça dos Enfermeiros, 4 Lisboa 1000-001', 'Clinica São João'),
('567890123', 'Hugo Martins', '955555555', 'Rua das Cuidadeiras, 5 Lisboa 1000-001', 'Clinica São João'),
('678901234', 'Inês Sousa', '966666666', 'Avenida das Cuidadoras, 6 Lisboa 1000-001', 'Clinica São João'),
('789012345', 'João Costa', '977777777', 'Rua dos Anjos, 7 Cascais 2765-001', 'Clinica Esperança'),
('890123456', 'Mariana Rodrigues', '988888888', 'Avenida das Fadas, 8 Cascais 2765-001', 'Clinica Esperança'),
('901234567', 'Tiago Almeida', '911111222', 'Travessa dos Ursos, 9 Cascais 2765-001', 'Clinica Esperança'),
('012345678', 'Carla Pereira', '922222333', 'Praça das Abelhas, 10 Cascais 2765-001', 'Clinica Esperança'),
('123456789', 'António Fernandes', '933333444', 'Rua das Borboletas, 11 Cascais 2765-001', 'Clinica Esperança'),
('234567890', 'Sara Cardoso', '944444555', 'Avenida dos Elefantes, 12 Cascais 2765-001', 'Clinica Esperança'),
('345678901', 'Rui Oliveira', '955555666', 'Travessa dos Leões, 13 Sintra 2710-001', 'Clinica Saúde Feliz'),
('456789012', 'Catarina Rodrigues', '966666777', 'Praça dos Tigres, 14 Sintra 2710-001', 'Clinica Saúde Feliz'),
('567890123', 'Paulo Pereira', '977777888', 'Rua dos Lobos, 15 Sintra 2710-001', 'Clinica Saúde Feliz'),
('678901234', 'Ana Martins', '988888999', 'Avenida das Girafas, 16 Sintra 2710-001', 'Clinica Saúde Feliz'),
('789012345', 'Daniel Costa', '911111000', 'Travessa dos Macacos, 17 Sintra 2710-001', 'Clinica Saúde Feliz'),
('890123456', 'Inês Sousa', '922222111', 'Praça dos Rinocerontes, 18 Sintra 2710-001', 'Clinica Saúde Feliz'),
('901234567', 'Miguel Silva', '933333222', 'Rua das Zebras, 19 Oeiras 2780-001', 'Clinica Bem-Estar'),
('012345678', 'Carolina Santos', '944444333', 'Avenida dos Tigres, 20 Oeiras 2780-001', 'Clinica Bem-Estar'),
('123456789', 'Filipe Sousa', '955555444', 'Travessa dos Ursos, 21 Oeiras 2780-001', 'Clinica Bem-Estar'),
('234567890', 'Sofia Oliveira', '966666555', 'Praça dos Leões, 22 Oeiras 2780-001', 'Clinica Bem-Estar'),
('345678901', 'Hélder Martins', '977777666', 'Rua dos Tigres, 23 Oeiras 2780-001', 'Clinica Bem-Estar'),
('456789012', 'Mónica Pereira', '988888777', 'Avenida das Girafas, 24 Oeiras 2780-001', 'Clinica Bem-Estar'),
('567890123', 'Ricardo Fernandes', '911111888', 'Travessa dos Rinocerontes, 25 Amadora 2650-001', 'Clinica Harmonia'),
('678901234', 'Andreia Rodrigues', '922222999', 'Praça dos Macacos, 26 Amadora 2650-001', 'Clinica Harmonia'),
('789012345', 'Diogo Costa', '933333000', 'Avenida dos Elefantes, 27 Amadora 2650-001', 'Clinica Harmonia'),
('890123456', 'Ana Oliveira', '944444111', 'Rua das Girafas, 28 Amadora 2650-001', 'Clinica Harmonia'),
('901234567', 'Marta Sousa', '955555222', 'Travessa dos Rinocerontes, 29 Amadora 2650-001', 'Clinica Harmonia'),
('012345678', 'Tiago Martins', '966666333', 'Praça dos Macacos, 30 Amadora 2650-001', 'Clinica Harmonia');

/*Populate medico*/
INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES
('123456789', 'Miguel Oliveira', '911111111', 'Rua dos Médicos, 1 Lisboa 1000-001', 'Clínica Geral'),
('234567890', 'Ana Santos', '922222222', 'Avenida das Consultas, 2 Lisboa 1000-001', 'Clínica Geral'),
('345678901', 'Pedro Martins', '933333333', 'Travessa das Consultas, 3 Lisboa 1000-001', 'Clínica Geral'),
('456789012', 'Rita Silva', '944444444', 'Praça dos Médicos, 4 Lisboa 1000-001', 'Clínica Geral'),
('567890123', 'Sara Ferreira', '955555555', 'Rua das Consultas, 5 Lisboa 1000-001', 'Clínica Geral'),
('678901234', 'João Sousa', '966666666', 'Avenida dos Médicos, 6 Lisboa 1000-001', 'Clínica Geral'),
('789012345', 'Mariana Costa', '977777777', 'Travessa dos Médicos, 7 Cascais 2765-001', 'Clínica Geral'),
('890123456', 'Tiago Rodrigues', '988888888', 'Praça das Consultas, 8 Cascais 2765-001', 'Clínica Geral'),
('901234567', 'Carla Oliveira', '911111222', 'Rua dos Consultórios, 9 Cascais 2765-001', 'Clínica Geral'),
('012345678', 'Hugo Costa', '922222333', 'Avenida dos Médicos, 10 Cascais 2765-001', 'Clínica Geral'),
('123456789', 'Inês Pereira', '933333444', 'Travessa das Consultas, 11 Cascais 2765-001', 'Clínica Geral'),
('234567890', 'António Fernandes', '944444555', 'Praça dos Médicos, 12 Cascais 2765-001', 'Clínica Geral'),
('345678901', 'Marta Rodrigues', '955555666', 'Rua das Consultas, 13 Sintra 2710-001', 'Clínica Geral'),
('456789012', 'Rui Almeida', '966666777', 'Avenida dos Médicos, 14 Sintra 2710-001', 'Clínica Geral'),
('567890123', 'Ana Santos', '977777888', 'Travessa dos Médicos, 15 Sintra 2710-001', 'Clínica Geral'),
('678901234', 'Daniel Costa', '988888999', 'Praça das Consultas, 16 Sintra 2710-001', 'Clínica Geral'),
('789012345', 'Miguel Silva', '911111000', 'Rua dos Consultórios, 17 Sintra 2710-001', 'Clínica Geral'),
('890123456', 'Inês Sousa', '922222111', 'Avenida dos Médicos, 18 Sintra 2710-001', 'Clínica Geral'),
('901234567', 'Sofia Oliveira', '933333222', 'Travessa das Consultas, 19 Oeiras 2780-001', 'Clínica Geral'),
('012345678', 'João Fernandes', '944444333', 'Praça dos Médicos, 20 Oeiras 2780-001', 'Clínica Geral'),
('567890123', 'Miguel Costa', '922222777', 'Avenida dos Pediatras, 34 Sintra 2710-001', 'Pediatria'),
('678901234', 'Ana Sousa', '933333888', 'Travessa dos Pediatras, 35 Sintra 2710-001', 'Pediatria'),
('789012345', 'Rui Santos', '944444999', 'Praça dos Pediatras, 36 Sintra 2710-001', 'Pediatria'),
('890123456', 'Carla Oliveira', '955555000', 'Rua dos Oftalmologistas, 37 Oeiras 2780-001', 'Oftalmologia'),
('901234567', 'Tiago Rodrigues', '966666111', 'Avenida dos Oftalmologistas, 38 Oeiras 2780-001', 'Oftalmologia'),
('012345678', 'Inês Fernandes', '977777222', 'Travessa dos Oftalmologistas, 39 Oeiras 2780-001', 'Oftalmologia'),
('123456789', 'João Almeida', '988888333', 'Praça dos Oftalmologistas, 40 Oeiras 2780-001', 'Oftalmologia'),
('234567890', 'Sofia Martins', '911111444', 'Rua dos Dermatologistas, 41 Oeiras 2780-001', 'Dermatologia'),
('345678901', 'Daniel Costa', '922222555', 'Avenida dos Dermatologistas, 42 Oeiras 2780-001', 'Dermatologia'),
('456789012', 'Mariana Silva', '933333666', 'Travessa dos Dermatologistas, 43 Oeiras 2780-001', 'Dermatologia'),
('567890123', 'Tiago Oliveira', '944444777', 'Praça dos Dermatologistas, 44 Oeiras 2780-001', 'Dermatologia'),
('678901234', 'Carla Sousa', '955555888', 'Rua dos Urologistas, 45 Oeiras 2780-001', 'Urologia'),
('789012345', 'Miguel Fernandes', '966666999', 'Avenida dos Urologistas, 46 Oeiras 2780-001', 'Urologia'),
('890123456', 'Inês Costa', '977777000', 'Travessa dos Urologistas, 47 Oeiras 2780-001', 'Urologia'),
('901234567', 'Pedro Almeida', '988888111', 'Praça dos Urologistas, 48 Oeiras 2780-001', 'Urologia'),
('012345678', 'Sara Oliveira', '911111222', 'Rua dos Otorrinolaringologistas, 49 Oeiras 2780-001', 'Otorrinolaringologia'),
('123456789', 'Rui Costa', '922222333', 'Avenida dos Otorrinolaringologistas, 50 Oeiras 2780-001', 'Otorrinolaringologia'),
('234567890', 'Ana Silva', '933333444', 'Travessa dos Otorrinolaringologistas, 51 Oeiras 2780-001', 'Otorrinolaringologia'),
('345678901', 'Marta Rodrigues', '944444555', 'Praça dos Otorrinolaringologistas, 52 Oeiras 2780-001', 'Otorrinolaringologia'),
('456789012', 'João Santos', '955555666', 'Rua dos Neurologistas, 53 Oeiras 2780-001', 'Neurologia'),
('567890123', 'Carolina Ferreira', '966666777', 'Avenida dos Neurologistas, 54 Oeiras 2780-001', 'Neurologia'),
('678901234', 'Tiago Almeida', '977777888', 'Travessa dos Neurologistas, 55 Oeiras 2780-001', 'Neurologia'),
('789012345', 'Inês Oliveira', '988888999', 'Praça dos Neurologistas, 56 Oeiras 2780-001', 'Neurologia'),
('890123456', 'Ricardo Costa', '911111000', 'Rua dos Ginecologistas, 57 Oeiras 2780-001', 'Ginecologia'),
('901234567', 'Ana Martins', '922222111', 'Avenida dos Ginecologistas, 58 Oeiras 2780-001', 'Ginecologia'),
('012345678', 'Miguel Pereira', '933333222', 'Travessa dos Ginecologistas, 59 Oeiras 2780-001', 'Ginecologia'),
('123456789', 'Sara Almeida', '944444333', 'Praça dos Ginecologistas, 60 Oeiras 2780-001', 'Ginecologia'),
('234567890', 'Tiago Fernandes', '955555444', 'Rua dos Geriatras, 61 Oeiras 2780-001', 'Ortopedia'),
('345678901', 'Inês Costa', '966666555', 'Avenida dos Geriatras, 62 Oeiras 2780-001', 'Ortopedia'),
('456789012', 'Marta Oliveira', '977777666', 'Travessa dos Geriatras, 63 Oeiras 2780-001', 'Ortopedia'),
('567890123', 'Rui Santos', '988888777', 'Praça dos Geriatras, 64 Oeiras 2780-001', 'Ortopedia'),
('678901234', 'Carla Sousa', '911111888', 'Rua dos Endocrinologistas, 65 Oeiras 2780-001', 'Cardiologia'),
('789012345', 'Miguel Fernandes', '922222999', 'Avenida dos Endocrinologistas, 66 Oeiras 2780-001', 'Cardiologia'),
('890123456', 'Inês Costa', '933333000', 'Travessa dos Endocrinologistas, 67 Oeiras 2780-001', 'Cardiologia'),
('901234567', 'Pedro Almeida', '944444111', 'Praça dos Endocrinologistas, 68 Oeiras 2780-001', 'Cardiologia');

/*Populate trabalha*/
/* É necessário na mesma depois verificar se cada clínica tem pelo menos 8 médicos em cada dia da semana */
CREATE OR REPLACE FUNCTION populate_trabalha() RETURNS VOID AS $$
DECLARE
    cursor_medico CURSOR FOR SELECT nif FROM medico;
    nif_medico CHAR(9);
    dia_semana SMALLINT;
BEGIN
    -- Loop through all medicos
    OPEN cursor_medico;
    LOOP
        FETCH cursor_medico INTO nif_medico;
        EXIT WHEN NOT FOUND;

        -- Randomly select 3 clinicas
        SELECT nome FROM clinica ORDER BY RANDOM() LIMIT 3 AS clinicas_frequentadas;

        -- For each day of the week, assign one of the 3 clinicas to the medico
        FOR dia_semana IN 0..6 LOOP

            -- Select a clinica from the 3 clinicas
            SELECT clinicas_frequentadas[1 + (dia_semana % 3)] INTO nome_clinica;

            INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES
            (nif_medico, nome_clinica, dia_semana);
        END LOOP;
    END LOOP;
END $$;

SELECT populate_trabalha();

/*Populate paciente*/
-- Generate 5000 patients
INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES
('123456789', '123456789', 'Miguel Oliveira', '911111111', 'Rua dos Médicos, 1 Lisboa 1000-001', '1990-01-01'),
('234567890', '234567890', 'Ana Santos', '922222222', 'Avenida das Consultas, 2 Lisboa 1000-001', '1991-02-02'),
('345678901', '345678901', 'Pedro Martins', '933333333', 'Travessa das Consultas, 3 Lisboa 1000-001', '1992-03-03'),
('456789012', '456789012', 'Rita Silva', '944444444', 'Praça dos Médicos, 4 Lisboa 1000-001', '1993-04-04'),
('567890123', '567890123', 'Sara Ferreira', '955555555', 'Rua das Consultas, 5 Lisboa 1000-001', '1994-05-05'),
('678901234', '678901234', 'João Sousa', '966666666', 'Avenida dos Médicos, 6 Lisboa 1000-001', '1995-06-06'),
('789012345', '789012345', 'Mariana Costa', '977777777', 'Travessa dos Médicos, 7 Cascais 2765-001', '1996-07-07'),
('890123456', '890123456', 'Tiago Rodrigues', '988888888', 'Praça das Consultas, 8 Cascais 2765-001', '1997-08-08'),
('901234567', '901234567', 'Carla Oliveira', '911111222', 'Rua dos Consultórios, 9 Cascais 2765-001', '1998-09-09'),
('012345678', '012345678', 'Hugo Costa', '922222333', 'Avenida dos Médicos, 10 Cascais 2765-001', '1999-10-10'),
('123456789', '123456789', 'Inês Pereira', '933333444', 'Travessa das Consultas, 11 Cascais 2765-001', '2000-11-11'),
('234567890', '234567890', 'António Fernandes', '944444555', 'Praça dos Médicos, 12 Cascais 2765-001', '2001-12-12'),
('345678901', '345678901', 'Marta Rodrigues', '955555666', 'Rua das Consultas, 13 Sintra 2710-001', '2002-01-13'),
('456789012', '456789012', 'Rui Almeida', '966666777', 'Avenida dos Médicos, 14 Sintra 2710-001', '2003-02-14'),
('567890123', '567890123', 'Ana Santos', '977777888', 'Travessa dos Médicos, 15 Sintra 2710-001', '2004-03-15'),
('678901234', '678901234', 'Daniel Costa', '988888999', 'Praça das Consultas, 16 Sintra 2710-001', '2005-04-16'),
('789012345', '789012345', 'Miguel Silva', '911111000', 'Rua dos Consultórios, 17 Sintra 2710-001', '2006-05-17'),
('890123456', '890123456', 'Inês Sousa', '922222111', 'Avenida dos Médicos, 18 Sintra 2710-001', '2007-06-18'),
('901234567', '901234567', 'Sofia Oliveira', '933333222', 'Travessa das Consultas, 19 Oeiras 2780-001', '2008-07-19'),
('012345678', '012345678', 'João Fernandes', '944444333', 'Praça dos Médicos, 20 Oeiras 2780-001', '2009-08-20'),
('123456789', '123456789', 'Miguel Oliveira', '911111111', 'Rua dos Médicos, 1 Lisboa 1000-001', '1990-01-01'),
('234567890', '234567890', 'Ana Santos', '922222222', 'Avenida das Consultas, 2 Lisboa 1000-001', '1991-02-02'),
('345678901', '345678901', 'Pedro Martins', '933333333', 'Travessa das Consultas, 3 Lisboa 1000-001', '1992-03-03'),
('456789012', '456789012', 'Rita Silva', '944444444', 'Praça dos Médicos, 4 Lisboa 1000-001', '1993-04-04'),
('567890123', '567890123', 'Sara Ferreira', '955555555', 'Rua das Consultas, 5 Lisboa 1000-001', '1994-05-05'),
('678901234', '678901234', 'João Sousa', '966666666', 'Avenida dos Médicos, 6 Lisboa 1000-001', '1995-06-06'),
('789012345', '789012345', 'Mariana Costa', '977777777', 'Travessa dos Médicos, 7 Cascais 2765-001', '1996-07-07'),
('890123456', '890123456', 'Tiago Rodrigues', '988888888', 'Praça das Consultas, 8 Cascais 2765-001', '1997-08-08'),
('901234567', '901234567', 'Carla Oliveira', '911111222', 'Rua dos Consultórios, 9 Cascais 2765-001', '1998-09-09'),
('012345678', '012345678', 'Hugo Costa', '922222333', 'Avenida dos Médicos, 10 Cascais 2765-001', '1999-10-10'),
('123456789', '123456789', 'Inês Pereira', '933333444', 'Travessa das Consultas, 11 Cascais 2765-001', '2000-11-11'),
('234567890', '234567890', 'António Fernandes', '944444555', 'Praça dos Médicos, 12 Cascais 2765-001', '2001-12-12'),
('345678901', '345678901', 'Marta Rodrigues', '955555666', 'Rua das Consultas, 13 Sintra 2710-001', '2002-01-13'),
('456789012', '456789012', 'Rui Almeida', '966666777', 'Avenida dos Médicos, 14 Sintra 2710-001', '2003-02-14'),
('567890123', '567890123', 'Ana Santos', '977777888', 'Travessa dos Médicos, 15 Sintra 2710-001', '2004-03-15'),
('678901234', '678901234', 'Daniel Costa', '988888999', 'Praça das Consultas, 16 Sintra 2710-001', '2005-04-16'),
('789012345', '789012345', 'Miguel Silva', '911111000', 'Rua dos Consultórios, 17 Sintra 2710-001', '2006-05-17'),
('890123456', '890123456', 'Inês Sousa', '922222111', 'Avenida dos Médicos, 18 Sintra 2710-001', '2007-06-18'),
('901234567', '901234567', 'Sofia Oliveira', '933333222', 'Travessa das Consultas, 19 Oeiras 2780-001', '2008-07-19'),
('012345678', '012345678', 'João Fernandes', '944444333', 'Praça dos Médicos, 20 Oeiras 2780-001', '2009-08-20'),
('123456789', '123456789', 'Miguel Oliveira', '911111111', 'Rua dos Médicos, 1 Lisboa 1000-001', '1990-01-01'),
('234567890', '234567890', 'Ana Santos', '922222222', 'Avenida das Consultas, 2 Lisboa 1000-001', '1991-02-02'),
('345678901', '345678901', 'Pedro Martins', '933333333', 'Travessa das Consultas 3 Lisboa 1000-001', '1992-03-03'),
('456789012', '456789012', 'Rita Silva', '944444444', 'Praça dos Médicos, 4 Lisboa 1000-001', '1993-04-04'),
('567890123', '567890123', 'Sara Ferreira', '955555555', 'Rua das Consultas, 5 Lisboa 1000-001', '1994-05-05'),
('678901234', '678901234', 'João Sousa', '966666666', 'Avenida dos Médicos, 6 Lisboa 1000-001', '1995-06-06'),
('789012345', '789012345', 'Mariana Costa', '977777777', 'Travessa dos Médicos, 7 Cascais 2765-001', '1996-07-07'),
('890123456', '890123456', 'Tiago Rodrigues', '988888888', 'Praça das Consultas, 8 Cascais 2765-001', '1997-08-08'),
('901234567', '901234567', 'Carla Oliveira', '911111222', 'Rua dos Consultórios, 9 Cascais 2765-001', '1998-09-09'),
('012345678', '012345678', 'Hugo Costa', '922222333', 'Avenida dos Médicos, 10 Cascais 2765-001', '1999-10-10'),
('123456789', '123456789', 'Inês Pereira', '933333444', 'Travessa das Consultas, 11 Cascais 2765-001', '2000-11-11'),
('234567890', '234567890', 'António Fernandes', '944444555', 'Praça dos Médicos, 12 Cascais 2765-001', '2001-12-12'),
('345678901', '345678901', 'Marta Rodrigues', '955555666', 'Rua das Consultas, 13 Sintra 2710-001', '2002-01-13'),
('456789012', 'Rui Almeida', '966666777', 'Avenida dos Médicos, 14 Sintra 2710-001', '2003-02-14'),
('567890123', 'Ana Santos', '977777888', 'Travessa dos Médicos, 15 Sintra 2710-001', '2004-03-15'),
('678901234', 'Daniel Costa', '988888999', 'Praça das Consultas, 16 Sintra 2710-001', '2005-04-16'),
('789012345', 'Miguel Silva', '911111000', 'Rua dos Consultórios, 17 Sintra 2710-001', '2006-05-17'),
('890123456', 'Inês Sousa', '922222111', 'Avenida dos Médicos, 18 Sintra 2710-001', '2007-06-18'),
('901234567', 'Sofia Oliveira', '933333222', 'Travessa das Consultas, 19 Oeiras 2780-001', '2008-07-19'),
('012345678', 'João Fernandes', '944444333', 'Praça dos Médicos, 20 Oeiras 2780-001', '2009-08-20'),
('123456789', 'Miguel Oliveira', '911111111', 'Rua dos Médicos, 1 Lisboa 1000-001', '1990-01-01'),
('234567890', 'Ana Santos', '922222222', 'Avenida das Consultas, 2 Lisboa 1000-001', '1991-02-02'),
('345678901', 'Pedro Martins', '933333333', 'Travessa das Consultas, 3 Lisboa 1000-001', '1992-03-03'),
('456789012', 'Rita Silva', '944444444', 'Praça dos Médicos, 4 Lisboa 1000-001', '1993-04-04'),
('567890123', 'Sara Ferreira', '955555555', 'Rua das Consultas, 5 Lisboa 1000-001', '1994-05-05'),
('678901234', 'João Sousa', '966666666', 'Avenida dos Médicos, 6 Lisboa 1000-001', '1995-06-06'),
('789012345', 'Mariana Costa', '977777777', 'Travessa dos Médicos, 7 Cascais 2765-001', '1996-07-07'),
('890123456', 'Tiago Rodrigues', '988888888', 'Praça das Consultas, 8 Cascais 2765-001', '1997-08-08'),
('901234567', 'Carla Oliveira', '911111222', 'Rua dos Consultórios, 9 Cascais 2765-001', '1998-09-09'),
('012345678', 'Hugo Costa', '922222333', 'Avenida dos Médicos, 10 Cascais 2765-001', '1999-10-10'),
('123456789', 'Inês Pereira', '933333444', 'Travessa das Consultas, 11 Cascais 2765-001', '2000-11-11'),
('234567890', 'António Fernandes', '944444555', 'Praça dos Médicos, 12 Cascais 2765-001', '2001-12-12'),
('345678901', 'Marta Rodrigues', '955555666', 'Rua das Consultas, 13 Sintra 2710-001', '2002-01-13'),
('456789012', 'Rui Almeida', '966666777', 'Avenida dos Médicos, 14 Sintra 2710-001', '2003-02-14'),
('567890123', 'Ana Santos', '977777888', 'Travessa dos Médicos, 15 Sintra 2710-001', '2004-03-15'),
('678901234', 'Daniel Costa', '988888999', 'Praça das Consultas, 16 Sintra 2710-001', '2005-04-16'),
('789012345', 'Miguel Silva', '911111000', 'Rua dos Consultórios, 17 Sintra 2710-001', '2006-05-17'),
('890123456', 'Inês Sousa', '922222111', 'Avenida dos Médicos, 18 Sintra 2710-001', '2007-06-18'),
('901234567', 'Sofia Oliveira', '933333222', 'Travessa das Consultas, 19 Oeiras 2780-001', '2008-07-19'),
('012345678', 'João Fernandes', '944444333', 'Praça dos Médicos, 20 Oeiras 2780-001', '2009-08-20'),
('123456789', 'Miguel Oliveira', '911111111', 'Rua dos Médicos, 1 Lisboa 1000-001', '1990-01-01'),
('234567890', 'Ana Santos', '922222222', 'Avenida das Consultas, 2 Lisboa 1000-001', '1991-02-02'),
('345678901', 'Pedro Martins', '933333333', 'Travessa das Consultas, 3 Lisboa 1000-001', '1992-03-03'),
('456789012', 'Rita Silva', '944444444', 'Praça dos Médicos, 4 Lisboa 1000-001', '1993-04-04'),
('567890123', 'Sara Ferreira', '955555555', 'Rua das Consultas, 5 Lisboa 1000-001', '1994-05-05'),
('678901234', 'João Sousa', '966666666', 'Avenida dos Médicos, 6 Lisboa 1000-001', '1995-06-06'),
('789012345', 'Mariana Costa', '977777777', 'Travessa dos Médicos, 7 Cascais 2765-001', '1996-07-07'),
('890123456', 'Tiago Rodrigues', '988888888', 'Praça das Consultas, 8 Cascais 2765-001', '1997-08-08'),
('901234567', 'Carla Oliveira', '911111222', 'Rua dos Consultórios, 9 Cascais 2765-001', '1998-09-09'),
('012345678', 'Hugo Costa', '922222333', 'Avenida dos Médicos, 10 Cascais 2765-001', '1999-10-10'),
('123456789', 'Inês Pereira', '933333444', 'Travessa das Consultas, 11 Cascais 2765-001', '2000-11-11'),
('234567890', 'António Fernandes', '944444555', 'Praça dos Médicos, 12 Cascais 2765-001', '2001-12-12'),
('345678901', 'Marta Rodrigues', '955555666', 'Rua das Consultas, 13 Sintra 2710-001', '2002-01-13'),
('456789012', 'Rui Almeida', '966666777', 'Avenida dos Médicos, 14 Sintra 2710-001', '2003-02-14'),
('567890123', 'Ana Santos', '977777888', 'Travessa dos Médicos, 15 Sintra 2710-001', '2004-03-15'),
('678901234', 'Daniel Costa', '988888999', 'Praça das Consultas, 16 Sintra 2710-001', '2005-04-16'),
('789012345', 'Miguel Silva', '911111000', 'Rua dos Consultórios, 17 Sintra 2710-001', '2006-05-17'),
('890123456', 'Inês Sousa', '922222111', 'Avenida dos Médicos, 18 Sintra 2710-001', '2007-06-18'),
('901234567', 'Sofia Oliveira', '933333222', 'Travessa das Consultas, 19 Oeiras 2780-001', '2008-07-19'),
('012345678', 'João Fernandes', '944444333', 'Praça dos Médicos, 20 Oeiras 2780-001', '2009-08-20'),
('123456789', 'Miguel Oliveira', '911111111', 'Rua dos Médicos, 1 Lisboa 1000-001', '1990-01-01'),
('234567890', 'Ana Santos', '922222222', 'Avenida das Consultas, 2 Lisboa 1000-001', '1991-02-02'),
('345678901', 'Pedro Martins', '933333333', 'Travessa das Consultas, 3 Lisboa 1000-001', '1992-03-03'),
('456789012', 'Rita Silva', '944444444', 'Praça dos Médicos, 4 Lisboa 1000-001', '1993-04-04'),
('567890123', 'Sara Ferreira', '955555555', 'Rua das Consultas, 5 Lisboa 1000-001', '1994-05-05'),
('678901234', 'João Sousa', '966666666', 'Avenida dos Médicos, 6 Lisboa 1000-001', '1995-06-06'),
('789012345', 'Mariana Costa', '977777777', 'Travessa dos Médicos, 7 Cascais 2765-001', '1996-07-07'),
('890123456', 'Tiago Rodrigues', '988888888', 'Praça das Consultas, 8 Cascais 2765-001', '1997-08-08'),
('901234567', 'Carla Oliveira', '911111222', 'Rua dos Consultórios, 9 Cascais 2765-001', '1998-09-09'),
('012345678', 'Hugo Costa', '922222333', 'Avenida dos Médicos, 10 Cascais 2765-001', '1999-10-10'),
('123456789', 'Inês Pereira', '933333444', 'Travessa das Consultas, 11 Cascais 2765-001', '2000-11-11'),
('234567890', 'António Fernandes', '944444555', 'Praça dos Médicos, 12 Cascais 2765-001', '2001-12-12'),
('345678901', 'Marta Rodrigues', '955555666', 'Rua das Consultas, 13 Sintra 2710-001', '2002-01-13');