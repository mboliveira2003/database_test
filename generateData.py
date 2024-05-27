import random
import string
import os

# Seed fixada para garantir que os dados são sempre os mesmos.
random.seed(0)

# Lista de 5 localidades de Lisboa, que serão associadas às clínicas, profissionais de saúde e pacientes.
localidades = ['Lisboa', 'Oeiras', 'Cascais', 'Sintra', 'Amadora']

############################################################################################################

# O objeto clínica tem um nome, um telefone e uma morada.
class Clinica:
    def __init__(self, nome, telefone, morada):
        self.nome = nome
        self.telefone = telefone
        self.morada = morada

    def __str__(self):
        return "Nome: " + self.nome + "\nTelefone: " + self.telefone + "\nMorada: " + self.morada

# Objeto para registar as clínicas criadas.
clinicas = []

# Cria uma tabela com 5 clínicas, associando-as a cada uma das 5 localidades criadas, e guarda num ficheiro csv.
def generateClinicas():
    for i in range(5):
        nome = 'Clinica ' + str(i+1)
        telefone = '9' + ''.join(random.choices(string.digits, k=8))
        morada = 'Rua ' + str(i+1) + ' Piso ' + str(i+1) + ' ' + ''.join(random.choices(string.digits, k=4)) + '-' +  ''.join(random.choices(string.digits, k=3)) + ' ' + localidades[i]
        clinicas.append(Clinica(nome, telefone, morada))
    
    with open('./csv_files/clinicas.csv', 'w') as file:
        for clinica in clinicas:
            file.write(clinica.nome + "," + clinica.telefone + "," + clinica.morada + "\n")

############################################################################################################

# O objeto enfermeiro tem um nif, um nome, um telefone, uma morada e uma clínica, onde trabalha.
class Enfermeiro:
    def __init__(self, nif, nome, telefone, morada, clinica):
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.clinica = clinica

    def __str__(self):
        return "NIF: " + self.nif + "\nNome: " + self.nome + "\nTelefone: " + self.telefone + "\nMorada: " + self.morada + "\nClinica: " + self.clinica

# Objeto para registar os enfermeiros criados.
enfermeiros = []   

# Cria uma tabela de enfermeiros, iterando pelas 5 clínicas registada em clinicas e associando a cada 6 enfermeiros diferentes.
# Guarda a tabela criada num ficheiro csv.
def generateEnfermeiros():
    enfermeiro_counter = 0
    for clinica in clinicas:
        for i in range(6):
            nif = ''.join(random.choices(string.digits, k=9))
            nome = 'Enfermeiro ' + str(enfermeiro_counter+1)
            telefone = '9' + ''.join(random.choices(string.digits, k=8))
            morada = 'Rua ' + str(i+1) + ' Piso ' + str(i+1) + ' ' + ''.join(random.choices(string.digits, k=4)) + '-' +  ''.join(random.choices(string.digits, k=3)) + ' ' + localidades[i%5]
            enfermeiros.append(Enfermeiro(nif, nome, telefone, morada, clinica.nome))
            enfermeiro_counter += 1
    
    with open('./csv_files/enfermeiros.csv', 'w') as file:
        for enfermeiro in enfermeiros:
            file.write(enfermeiro.nif + "," + enfermeiro.nome + "," + enfermeiro.telefone + "," + enfermeiro.morada + "," + enfermeiro.clinica + "\n")

############################################################################################################

# O objeto medico tem um nif, um nome, um telefone, uma morada e uma especialidade.
class Medico:
    def __init__(self, nif, nome, telefone, morada, especialidade):
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.especialidade = especialidade

    def __str__(self):
        return "NIF: " + self.nif + "\nNome: " + self.nome + "\nTelefone: " + self.telefone + "\nMorada: " + self.morada + "\nEspecialidade: " + self.especialidade

# Objeto para registar os médicos criados.
medicos = []   

# Cria uma tabela com 60 médicos, 20 dos quais têm a especialidade de clínica geral,
# 20 de ortopedia 20 de cardiologia. Guarda a tabela gerada num ficheiro csv.
def generateMedicos():
    especialidades = ['clinica geral', 'ortopedia', 'cardiologia']
    for i in range(60):
        nif = ''.join(random.choices(string.digits, k=9))
        nome = 'Medico ' + str(i+1)
        telefone = '9' + ''.join(random.choices(string.digits, k=8))
        morada = 'Rua ' + str(i+1) + ' Piso ' + str(i+1) + ' ' + ''.join(random.choices(string.digits, k=4)) + '-' +  ''.join(random.choices(string.digits, k=3)) + ' ' + localidades[i%5]
        especialidade = especialidades[i//20]
        medicos.append(Medico(nif, nome, telefone, morada, especialidade))
    
    with open('./csv_files/medicos.csv', 'w') as file:
        for medico in medicos:
            file.write(medico.nif + "," + medico.nome + "," + medico.telefone + "," + medico.morada + "," + medico.especialidade + "\n")

############################################################################################################

# O objeto paciente tem um ssn, um nif, um nome, um telefone, uma morada e uma data de nascimento.
class Paciente:
    def __init__(self, ssn, nif, nome, telefone, morada, dataNascimento):
        self.ssn = ssn
        self.nif = nif
        self.nome = nome
        self.telefone = telefone
        self.morada = morada
        self.dataNascimento = dataNascimento

    def __str__(self):
        return "SSN: " + self.ssn + "\nNIF: " + self.nif + "\nNome: " + self.nome + "\nTelefone: " + self.telefone + "\nMorada: " + self.morada + "\nData de Nascimento: " + self.dataNascimento

# Objeto para registar os pacientes criados.
pacientes = [] 

# Cria uma tabela com 5000 pacientes e guarda num ficheiro csv.
def generatePacientes():
    for i in range(5000):
        ssn = ''.join(random.choices(string.digits, k=11))
        nif = ''.join(random.choices(string.digits, k=9))
        nome = 'Paciente ' + str(i+1)
        telefone = '9' + ''.join(random.choices(string.digits, k=8))
        morada = 'Rua ' + str(i+1) + ' Piso ' + str(i+1) + ' ' + ''.join(random.choices(string.digits, k=4)) + '-' +  ''.join(random.choices(string.digits, k=3)) + ' ' + localidades[i%5]
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(1900, 2022)
        dataNascimento = f"{year:04d}-{month:02d}-{day:02d}"
        pacientes.append(Paciente(ssn, nif, nome, telefone, morada, dataNascimento))
    
    with open('./csv_files/pacientes.csv', 'w') as file:
        for paciente in pacientes:
            file.write(paciente.ssn + "," + paciente.nif + "," + paciente.nome + "," + paciente.telefone + "," + paciente.morada + "," + paciente.dataNascimento + "\n")

############################################################################################################

# O objeto trabalha inclui um nif, correspondente ao nif de um médico, um nome,
# correspondente ao nome de uma clínica e um dia da semana (representado por um inteiro de 0 a 6),
# correspondente ao dia da semana em que o médico trabalha nessa clínica.
class Trabalha:
    def __init__(self, nif, nome, diaSemana):
        self.nif = nif
        self.nome = nome
        self.diaSemana = diaSemana

    def __str__(self):
        return "NIF: " + self.nif + "\nNome: " + self.nome + "\nDia da Semana: " + str(self.diaSemana)

# Objeto para registar os trabalhos criados
trabalha = []

# Cria uma tabela trabalha, iterando sobre todos os dias da semana e posteriormente sobre todas as clínicas,
# associando a cada par dia da semana e clínica, 10 médicos diferentes. Assim assegura-se que a cada dia da semana
# há pelo menos 8 médicos em cada clínica. As iterações (350) também são suficientes para garantir que todos os médicos
# trabalham em pelo menos 2 clínicas diferentes. Guarda a tabela criada num ficheiro csv.
def generateTrabalha():
    medico_pointer = 0
    for i in range(7):
        for clinica in clinicas:
            for j in range(10):
                medico = medicos[medico_pointer%60]
                trabalha.append(Trabalha(medico.nif, clinica.nome, i))
                medico_pointer += 1
    
    with open('./csv_files/trabalha.csv', 'w') as file:
        for t in trabalha:
            file.write(t.nif + "," + t.nome + "," + str(t.diaSemana) + "\n")

############################################################################################################

# O objeto consulta tem um id, um ssn, correspondente ao ssn de um paciente, um nif, correspondente ao nif de um médico,
# um nome, correspondente ao nome da clínica onde o médico trabalha no dia da consulta, uma data, uma hora e um codigo_sns,
# correspondente ao código da receita médica associada à consulta, se esta existir.
class Consulta:
    def __init__(self, id, ssn, nif, nome, data, hora, codigo_sns):
        self.id = id
        self.ssn = ssn
        self.nif = nif
        self.nome = nome
        self.data = data
        self.hora = hora
        self.codigo_sns = codigo_sns

    def __str__(self):
        return "ID: " + self.id + "\nSSN: " + self.ssn + "\nNIF: " + self.nif + "\nNome: " + self.nome + "\nData: " + self.data + "\nHora: " + self.hora

# Objeto para registar as consultas criadas
consultas = []

# Função para calcular o dia da semana de uma data, segundo a fórmula de Zeller.
def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    
    K = year % 100
    J = year // 100
    
    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7 
    
    return h-1 if h != 0 else 6

# Cria uma tabela consultas, iterando sobre (quase) todos os dias dos anos de 2023, 2024 e 2025 e posteriormente iterando sobre as 5 clínicas.
# Para cada dia e clínica, itera sobre todos os médicos que trabalham nesse dia na clínica. Para cada médico, associa a cada horário de 
# consulta possível (de 30 em 30 minutos entre as 8h e as 12h e as 14h e as 19h) um paciente diferente.
# 80% das consultas têm receita médica associada, sendo que para as restantes o código_sns é "null". Assim garante-se que em cada dia, 
# em cada clínica há pelo menos 8 médicos a trabalhar (10 médicos * 18 consultas diárias) e que cada médico tem pelo menos 2 consulta por dia.
# Para além disso o número de consultas totais por dia (5 clínicas * 10 médicos * 18 consultas diárias = 900 < 5000) é suficiente para garantir que cada paciente
# não tem duas consultas no mesmo dia.
# Guarda a tabela criada num ficheiro csv.
def generateConsultas():
    consulta_pointer = 0
    # Popular as consutas para 2023
    for year in range(2023, 2024):
        for month in range(1, 13):
            for day in range(1, 29):
                # Zeller's Congruence: fórmula para calcular o dia da semana (de 0 a 6) de uma data
                day_of_week = zellers_congruence(day, month, year)
                for clinica in clinicas:
                        # Ir à tabela trabalha ver quais os médicos que trabalham na clínica clinica no dia da semana i
                        medicos_available = [t.nif for t in trabalha if t.nome == clinica.nome and t.diaSemana == day_of_week]
                        for medico_nif in medicos_available:
                            for hour in range(8, 19):
                                for minute in range(0, 60, 30):
                                    if hour <= 12 or hour >= 14:
                                        ssn = pacientes[consulta_pointer%5000].ssn
                                        # Calcula uma distribuição binomial para decidir se a consulta tem receita médica associada
                                        if random.random() < 0.8:
                                            consultas.append(Consulta(str(consulta_pointer), ssn, medico_nif, clinica.nome, f"{year:04d}-{month:02d}-{day:02d}", f"{hour:02d}:{minute:02d}:00", ''.join(random.choices(string.digits, k=12))))
                                        else:
                                            consultas.append(Consulta(str(consulta_pointer), ssn, medico_nif, clinica.nome, f"{year:04d}-{month:02d}-{day:02d}", f"{hour:02d}:{minute:02d}:00", "null"))
                                        consulta_pointer += 1
    # Popular as consutas até meio de 2024
    for year in range(2024, 2025):
        for month in range(1, 6):
            for day in range(1, 29):
                # Zeller's Congruence: fórmula para calcular o dia da semana (de 0 a 6) de uma data
                day_of_week = zellers_congruence(day, month, year)
                for clinica in clinicas:
                        # Ir à tabela trabalha ver quais os médicos que trabalham na clínica clinica no dia da semana i
                        medicos_available = [t.nif for t in trabalha if t.nome == clinica.nome and t.diaSemana == day_of_week]
                        for medico_nif in medicos_available:
                            for hour in range(8, 19):
                                for minute in range(0, 60, 30):
                                    if hour < 12 or hour >= 14:
                                        ssn = pacientes[consulta_pointer%5000].ssn
                                        # Calcula uma distribuição binomial para decidir se a consulta tem receita médica associada
                                        if random.random() < 0.8:
                                            consultas.append(Consulta(str(consulta_pointer), ssn, medico_nif, clinica.nome, f"{year:04d}-{month:02d}-{day:02d}", f"{hour:02d}:{minute:02d}:00", ''.join(random.choices(string.digits, k=12))))
                                        else:
                                            consultas.append(Consulta(str(consulta_pointer), ssn, medico_nif, clinica.nome, f"{year:04d}-{month:02d}-{day:02d}", f"{hour:02d}:{minute:02d}:00", "null"))
                                        consulta_pointer += 1
    
    with open('./csv_files/consultas.csv', 'w') as file:
        for consulta in consultas:
            file.write(consulta.id + "," + consulta.ssn + "," + consulta.nif + "," + consulta.nome + "," + consulta.data + "," + consulta.hora + "," + consulta.codigo_sns + "\n")

############################################################################################################

# O objeto receita tem um código_sns, que está associado à consulta em que foi receitada,
# 1 a 6 medicamentos, correspondente aos nomes dos medicamentos receitados e as respetivas quantidades.
# As quantidades prescritas são geradas aleatoriamente entre 1 e 3.
class Receita:
    def __init__(self, codigo_sns, medicamento, quantidade):
        self.codigo_sns = codigo_sns
        self.medicamento = medicamento
        self.quantidade = quantidade

    def __str__(self):
        return "Código SNS: " + self.codigo_sns + "\nMedicamento: " + self.medicamento + "\nQuantidade: " + str(self.quantidade)
    
# O nome dos medicamentos deve ser escolhido dentro da seguinte lista.
medicamentos = [
    # Analgésicos e Anti-inflamatórios
    "Paracetamol (Tylenol)",
    "Ibuprofeno (Advil ou Motrin)",
    "Aspirina (AAS)",
    "Naproxeno (Aleve)",
    "Diclofenaco (Voltaren)",
    
    # Antibióticos
    "Amoxicilina (Amoxil)",
    "Azitromicina (Zithromax)",
    "Ciprofloxacina (Cipro)",
    "Doxiciclina (Vibramycin)",
    "Cefalexina (Keflex)",
    
    # Antidepressivos
    "Fluoxetina (Prozac)",
    "Sertralina (Zoloft)",
    "Amitriptilina (Elavil)",
    "Venlafaxina (Effexor)",
    "Citalopram (Celexa)",
    
    # Anti-hipertensivos
    "Losartana (Cozaar)",
    "Amlodipina (Norvasc)",
    "Enalapril (Vasotec)",
    "Metoprolol (Lopressor)",
    "Hidroclorotiazida (Microzide)",
    
    # Anti-histamínicos
    "Loratadina (Claritin)",
    "Cetirizina (Zyrtec)",
    "Difenidramina (Benadryl)",
    "Fexofenadina (Allegra)",
    "Clorfeniramina (Chlor-Trimeton)",
    
    # Antidiabéticos
    "Metformina (Glucophage)",
    "Glibenclamida (Diabeta)",
    "Sitagliptina (Januvia)",
    "Pioglitazona (Actos)",
    "Insulina",
    
    # Broncodilatadores
    "Salbutamol (Ventolin)",
    "Ipratropio (Atrovent)",
    "Formoterol (Foradil)",
    "Tiotropio (Spiriva)",
    "Salmeterol (Serevent)",
    
    # Antipsicóticos
    "Risperidona (Risperdal)",
    "Olanzapina (Zyprexa)",
    "Quetiapina (Seroquel)",
    "Aripiprazol (Abilify)",
    "Clozapina (Clozaril)",
    
    # Estatinas (para baixar colesterol)
    "Atorvastatina (Lipitor)",
    "Sinvastatina (Zocor)",
    "Rosuvastatina (Crestor)",
    "Pravastatina (Pravachol)",
    "Lovastatina (Mevacor)",
    
    # Anticoagulantes
    "Varfarina (Coumadin)",
    "Rivaroxabana (Xarelto)",
    "Apixabana (Eliquis)",
    "Dabigatrana (Pradaxa)",
    "Heparina"
]

# Objeto para registar as receitas criadas.
receitas = []

# Cria uma tabela de receitas, iterando por todas as entradas da tabela consulta em que o codigo_sns é diferente de "null".
# De seguida, itera por um número aleatório de 1 a 6 medicamentos diferentes e associa a cada medicamento uma quantidade
# inteira aleatória entre 1 e 3. Guarda a tabela criada num ficheiro csv.
def generateReceitas():
    medicamento_pointer = 0
    for consulta in consultas:
        if consulta.codigo_sns != "null":
            for i in range(random.randint(1, 6)):
                medicamento = medicamentos[medicamento_pointer%len(medicamentos)]
                quantidade = random.randint(1, 3)
                receitas.append(Receita(consulta.codigo_sns, medicamento, quantidade))
                medicamento_pointer += 1
    
    with open('./csv_files/receitas.csv', 'w') as file:
        for receita in receitas:
            file.write(receita.codigo_sns + "," + receita.medicamento + "," + str(receita.quantidade) + "\n")

############################################################################################################

# A classe observação tem um id, correspondente ao id da consulta em que foi registada, um parametro, correspondente ao nome 
# do parametro observado e um valor associado ao parâmetro. O valor pode ser "null" para parâmetros descritivos ou um float
# aleatório entre 0 e 1000 para parâmetros quantitativos.
class Observacao:
    def __init__(self, id, parametro, valor):
        self.id = id
        self.parametro = parametro
        self.valor = valor

    def __str__(self):
        return "ID: " + self.id + "\nParâmetro: " + self.parametro + "\nValor: " + str(self.valor)

# Os parâmetros descritivos podem ser escolhidos de dentro da seguinte lista, com 53 parâmetros diferentes. 
parametros_descritivos = [
    "Dor de cabeca",
    "Nausea",
    "Tontura",
    "Fadiga",
    "Dor no peito",
    "Falta de ar",
    "Febre",
    "Tosse",
    "Dor abdominal",
    "Diarreia",
    "Constipacao",
    "Dor nas articulacoes",
    "Inchaco",
    "Arrepios",
    "Sudorese",
    "Palpitacoes",
    "Irritacao na pele",
    "Prurido (coceira)",
    "Vomito",
    "Perda de apetite",
    "Ansiedade",
    "Depressao",
    "Insonia",
    "Perda de peso",
    "Ganho de peso",
    "Dificuldade para urinar",
    "Visao turva",
    "Dor de garganta",
    "Rouquidao",
    "Corrimento nasal",
    "Dor de dente",
    "Zumbido nos ouvidos",
    "Dificuldade de concentracao",
    "Letargia",
    "Dor muscular",
    "Desmaio",
    "Sensacao de fraqueza",
    "Alteracoes de humor",
    "Sensibilidade a luz",
    "Inquietacao",
    "Confusao mental",
    "Erupcao cutanea",
    "Tremores",
    "Desorientacao",
    "Rigidez muscular",
    "Edema",
    "Hemorragia",
    "Formigamento",
    "Parestesia",
    "Disfagia (dificuldade para engolir)",
    "Disfonia (alteracao da voz)",
    "Dismenorreia (colica menstrual)",
    "Poliuria (aumento da quantidade de urina)",
    "Nocturia (necessidade de urinar a noite)",
    "Cianose (coloracao azulada da pele)",
    "Alopecia (queda de cabelo)",
    "Hiperidrose (sudorese excessiva)"
]

# Os parâmetros quantitativos podem ser escolhidos de dentro da seguinte lista, com 22 parâmetros diferentes.
parametros_quantitativos = [
    "Pressao arterial (mmHg)",
    "Frequencia cardiaca (bpm)",
    "Temperatura corporal (Graus Celsius)",
    "Nivel de glicose no sangue (mg/dL)",
    "Saturacao de oxigenio (SpO2 percentagem)",
    "Peso corporal (kg)",
    "Altura (cm)",
    "Indice de Massa Corporal (IMC kg/m^2)",
    "Colesterol total (mg/dL)",
    "LDL (Colesterol ruim mg/dL)",
    "HDL (Colesterol bom mg/dL)",
    "Triglicerideos (mg/dL)",
    "Hemoglobina (g/dL)",
    "Hematocrito (percentagem)",
    "Contagem de leucocitos (celulas/micro Litros)",
    "Contagem de plaquetas (celulas/micro Litros)",
    "Taxa de Filtracao Glomerular (TFG mL/min/1.73m^2)",
    "Creatinina serica (mg/dL)",
    "Bilirrubina total (mg/dL)",
    "Enzimas hepaticas (AST/ALT U/L)",
    "Taxa de respiracao (respiracoes por minuto)",
    "Circunferencia abdominal (cm)"
]

# Objeto para registar as observações criadas
observacoes = []
    
# Cria a tabela observacao, iterando por todas as entradas da tabela consulta. De seguida, determina aleatoriamente
# um número de 1 a 5, que corresponderá ao número de parâmetros qualitativos a associar à consulta, e depois determina um número 
# aleatório de 0 a 3, que corresponderá ao número de parâmetros quantitativos a associar à consulta. A cada parâmetro qualitativo
# estará associado um valor de "null" e a cada parâmetro quantitativo estará associado um float aleatório entre 0 e 1000.
def generateObservacoes():
    parametros_descritivos_pointer = 0
    parametros_quantitativos_pointer = 0
    for consulta in consultas:
        for i in range(random.randint(1, 5)):
            parametro = parametros_descritivos[parametros_descritivos_pointer%len(parametros_descritivos)]
            observacoes.append(Observacao(consulta.id, parametro, "null"))
            parametros_descritivos_pointer += 1
        for i in range(random.randint(0, 3)):
            parametro = parametros_quantitativos[parametros_quantitativos_pointer%len(parametros_quantitativos)]
            observacoes.append(Observacao(consulta.id, parametro, random.uniform(0, 1000)))
            parametros_quantitativos_pointer += 1
    
    with open('./csv_files/observacoes.csv', 'w') as file:
        for observacao in observacoes:
            file.write(observacao.id + "," + observacao.parametro + "," + str(observacao.valor) + "\n")

############################################################################################################

# Função principal que chama todas as funções de geração de dados.
if __name__ == '__main__':

    # Create the directory csv_files if it does not exist
    if not os.path.exists('./csv_files'):
        os.makedirs('./csv_files')

    generateClinicas()
    generateEnfermeiros()
    generateMedicos()
    generatePacientes()
    generateTrabalha()
    generateConsultas()
    generateReceitas()
    generateObservacoes()

