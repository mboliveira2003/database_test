# Open file enfermeiros.csv and check if the first entry in each column is unique

import csv

def validateData2():
    with open('./csv_files/pacientes.csv', 'r') as file:
        reader = csv.reader(file)
        columns = {}
        for row in reader:
            for i in range(len(row)):
                if i not in columns:
                    columns[i] = []
                if row[i] in columns[i]:
                    print(f"Duplicate entry in column {i}: {row[i]}")
                columns[i].append(row[i])

# Check if the first entry of each row only has numbers

def validateData():
    with open('./csv_files/pacientes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row[0].isnumeric():
                print(f"Invalid entry in column 0: {row[0]}")
                print(row)
    


def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    
    K = year % 100
    J = year // 100
    
    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    
    return h



# From the file receitas.csv output the rows with more than 3 columns

def validateData3():
    with open('./csv_files/observacoes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 3:
                print(row)

validateData3()