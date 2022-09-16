'''
2.3) Para o segundo exercício, você deve criar um programa que realize uma cópia do arquivo "alunos.csv". 
Essa cópia deve ser um arquivo chamado "alunos_copia.csv".
'''
import csv 

with open('alunos.csv', 'r', encoding='utf-8') as arquivo_csv: #criar arquivo legivel
    leitor = csv.reader(arquivo_csv) #criar objetocsv.reader
    listAlunos = list(leitor) # convertendo objeto csv.reader em lista de listas
   
# Criando um arquivo:
with open('alunos_copia.csv', 'w', newline='') as new_arquivo:
    # Criando um Escritor:
    writer = csv.writer(new_arquivo)
    # Escrevendo os dados:
    writer.writerows(listAlunos)

# lendo o arquivo criado
with open('alunos_copia.csv', 'r', encoding='utf-8') as arquivo_csv: #criar arquivo legivel
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
            print(linha)