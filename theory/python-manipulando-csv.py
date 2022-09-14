# Exercicio cadastro de usuario:
import csv
# Criando um cabeçalho:
header = ['Nome ', 'Sobrenome ']

# Criando uma lista vazia para armazenar os dados recebidos atraves do input:
dados = []

# Input ao usuario sobre o que deseja fazer:
opc = input('\nO que deseja fazer?\n1 - Para cadastrar usuario \n0 - Sair\n')

# loop até que a resposta seja 0 para sair do loop:
while opc != '0':
    nome = input('Qual seu nome?\n')
    sobrenome = input('Qual seu sobrenome?\n')
    
    # Adicionando as duas variaveis nome e sobrenome na lista vazia.
    dados.append([nome, sobrenome])
    opc = input('O que deseja fazer?\n1 - Para cadastrar usuario \n0 - Sair\n')

print(dados)

# Criando um arquivo:
with open('cadastro_pesssoas.csv', 'w', newline='') as new_arquivo:
    # Criando um Escritor:
    writer = csv.writer(new_arquivo)
    # Escrevendo o cabeçalho:
    writer.writerow(header)
    # Escrevendo os dados:
    writer.writerows(dados)

# Fazendo a leitura do arquivo criado acima:
with open('cadastro_pesssoas.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
