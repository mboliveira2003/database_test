-- Populate table clinica with data in csv file clinicas.csv
COPY clinica FROM '/csv_files/clinicas.csv' DELIMITER ',' CSV;

-- Populate table enfermeiro with data in csv file enfermeiros.csv
COPY enfermeiro FROM '/csv_files/enfermeiros.csv' DELIMITER ',' CSV;

-- Populate table medico with data in csv file medicos.csv
COPY medico FROM '/csv_files/medicos.csv' DELIMITER ',' CSV;

-- Populate table trabalha with data in csv file trabalha.csv
COPY trabalha FROM '/csv_files/trabalha.csv' DELIMITER ',' CSV;

-- Populate table paciente with data in csv file pacientes.csv
COPY paciente FROM '/csv_files/pacientes.csv' DELIMITER ',' CSV;

-- Populate table consulta with data in csv file consultas.csv
COPY consulta FROM '/csv_files/consultas.csv' DELIMITER ',' CSV NULL AS 'null';

-- Populate table receita with data in csv file receitas.csv
COPY receita FROM '/csv_files/receitas.csv' DELIMITER ',' CSV;

-- Populate table observacao with data in csv file observacoes.csv
COPY observacao FROM '/csv_files/observacoes.csv' DELIMITER ',' CSV NULL AS 'null';

-- Select all data from table clinica
SELECT * FROM clinica;

