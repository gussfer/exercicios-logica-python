'''
3.1) Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5
perguntas onde a resposta só pode ser sim ou não:
a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados.
'''
# inicializando o contador
i = 0

a = input("Mora perto da vítima?: ")
while a.lower() != "sim" and a.lower() != "não":
    print('Por favor, responda somente "Sim" ou "Não"')
    a = input("Mora perto da vítima?: ")
if a.lower() == "sim":
    i += 1

b = input("Já trabalhou com a vítima?: ")
while b.lower() != "sim" and b.lower() != "não":
    print('Por favor, responda somente "Sim" ou "Não"')
    b = input("Já trabalhou com a vítima?: ")
if b.lower() == "sim":
    i += 1

c = input("Telefonou para a vítima?: ")
while c.lower() != "sim" and c.lower() != "não":
    print('Por favor, responda somente "Sim" ou "Não"')
    c = input("Telefonou para a vítima?: ")
if c.lower() == "sim":
   i += 1

d = input("Esteve no local do crime?: ")
while d.lower() != "sim" and d.lower() != "não":
    print('Por favor, responda somente "Sim" ou "Não"')
    d = input("Esteve no local do crime?: ")
if d.lower() == "sim":
    i += 1

e = input("Devia para a vítima?: ")
while e.lower() != "sim" and e.lower() != "não":
    print('Por favor, responda somente "Sim" ou "Não"')
    e = input("Devia para a vítima?: ")
if e.lower() == "sim":
    i += 1
print("")

# criação método case com dicionario python
def assassino():
    print("O investigado é o assassino")
def cumplice():
    print("O investigado é o cumplice")
def suspeito():
    print("O investigado é suspeito")
def liberado():
    print("O investigado pode ser liberado")
investigacao = {1:assassino , 2: cumplice, 3: suspeito, 4: liberado}

# criação da condenação baseado em condições
if i == 5:
    investigacao.get(1)()
if i == 4 or i == 3:
    investigacao.get(2)()
if i == 2:
    investigacao.get(3)()
if i < 2:
    investigacao.get(4)()