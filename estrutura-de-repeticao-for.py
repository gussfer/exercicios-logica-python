#For é comumente utilizado pra iteração de objetos
nomesPaises = ['Brasil', 'Peru', 'Argentina', 'Colômbia', 'Chile']
for pais in nomesPaises:
    print(pais)

nomesPaisesTupla = 'Brasil', 'Peru', 'Argentina', 'Colômbia', 'Chile'
for pais in nomesPaisesTupla:
    print(pais)

dadosCidade = {
    'Nome': 'São Paulo',
    'Estado': 'São Paulo',
    'Área (km²)' : 1521,
    'População (milhões)': 12.18
}
for chave in dadosCidade:
    print(f'{chave}: {dadosCidade[chave]}')

#Criar um range para manipulação de obejtos através do for
for posição in range(len(nomesPaises)):
    print(posição)
#Outros usos para o range
print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10, 3)))