'''
3 - Finalmente chegamos ao último exercício dessa sequência relacionada à manipulação de arquivos.
Neste exercício você deve criar um novo arquivo chamado "alunos_media.csv". 
Esse novo arquivo é uma cópia de "alunos.csv" porém com uma coluna a mais chamada 
"Média" que vai abrigar os valores das médias das provas de cada aluno da lista.
'''
#tratamento com biblioteca 'csv', nativa do python
import csv 

with open('alunos.csv', 'r', encoding='utf-8') as arquivo_csv: #criar arquivo legivel
    leitor = csv.reader(arquivo_csv, delimiter=',')

    dados = [] # criar dataSet com lista vazia 

    for i, linha in enumerate(leitor): # função enumerate adiciona um índice para a lista
            # isolando o header para adicionar a última 'coluna'
            if i == 0:
                linha.append('Media')
                # print(linha)
                header = list(linha)
                # print(dados)
            else:
                linha1 = [float(x) for x in linha[3:]] #converter os itens da lista em float
                linha.append(sum(linha1)/len(linha1)) # adiciona media das notas da prova de cada aluno
                dados.append(list(linha)) # adicionar lista oriunda da for ao dataSet

# Criando um arquivo:
with open('alunos_media.csv', 'w', newline='') as new_arquivo1:
    # Criando um Escritor:
    writer = csv.writer(new_arquivo1)
    # Escrevendo o header:
    writer.writerow(header)
    # Escrevendo os dados:
    writer.writerows(dados)