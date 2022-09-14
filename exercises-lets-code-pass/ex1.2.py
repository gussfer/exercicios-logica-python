'''
1.2) Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.
'''
import random

listaNumeros = random.sample(range(100),10) #gerar uma lista aleatória
print(listaNumeros)
novaLista = [x for x in listaNumeros if x%2 == 0] #cria uma nova lista com a condição imposta
print("Dessa lista de números, {} deles são pares".format(len(novaLista)))
# percorrendo a lista
# for x in novaLista:
#     print(x)