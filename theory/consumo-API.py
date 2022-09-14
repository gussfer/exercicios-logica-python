'''
Para consumo de uma API é necesário realizar uma requisição web simples (acessar uma rota web).
Tarefa: consumir uma API e converter o valor de R$ para US$
rates: retorna quanto cada moeda vale em comparação ao dolar
'''
import requests

url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)

dados = req.json()
print(dados)

valor_reais = float(input('Infome o valor em R$ que deseja converter\n'))
cotacao = dados['rates']['BRL'] # como json possui a estrutura de dicionário, podemos usar a localização deles para acessar um valor correspondente a chave 'rates'
print('R${:.2f} em dolar valem US$ {:.2f}'.format(valor_reais, (valor_reais/cotacao)))


