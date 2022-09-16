'''
1.3) Neste exercício você deve criar um programa que abra o arquivo
"alunos.csv" e imprima o conteúdo do arquivo linha a linha.
'''
# tratamento com pandas
import pandas as pd

alunos = pd.read_csv("alunos.csv")
print(alunos)
#display(alunos)# alternativa - alunos.style

#tratamento com biblioteca 'csv', nativa do python
import csv 
with open('alunos.csv', 'r', encoding='utf-8') as arquivo_csv: #criar arquivo legivel
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
            print(linha)