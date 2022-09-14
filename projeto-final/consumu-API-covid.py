import requests as r
import csv
# setando a requisição: A API alvo retorna um json. Cada dicionário contem chaves valores contendo dados no padrão chave-valor
url = 'https://api.covid19api.com/dayone/country/brazil'
req = r.get(url)
print(req.status_code)

# transformando a resposta da requisição em variável
raw_data = req.json()
print(raw_data[0:2])

# enxugando as informações para gerar um csv
final_data =[] #lista vazia
for obs in raw_data: #para cada item 'obs' do json, adicionar o valor correspondentes as chaves ['']
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

final_data.insert(0, ['Confirmados', 'Obitos', 'Recuperados', 'Ativos', 'Data']) # inserindo um header no csv

final_data

# manipulações dos dados - reduzindo data 
CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)): # para o indice dentro do range da posição 1 até o tam da lista
    final_data[i][DATA] = final_data[i][DATA][:10]
final_data

# Criando um arquivo:
with open('brasil-covid.csv', 'w', newline='') as new_arquivo:
    # Criando um Escritor:
    writer = csv.writer(new_arquivo)
    # Atribuindo os valores atuais ao arquivo csv:
    writer.writerow(final_data)

# manipulações dos dados - transformando string data em formato data (biblioteca DateTime) 
import datetime as dt
for i in range(1, len(final_data)): # para o indice dentro do range da posição 1 até o tam da lista
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA],'%Y-%m-%d') # função que retorna um objeto datetime ao inves de str

print(final_data)



