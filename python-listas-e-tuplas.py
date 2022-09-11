from collections import Counter
#Listas e Tuplas - tuplas não podem sofrer alterações
nomesPaises = ['Brasil', 'Brasil', 'Argentina', 'Colômbia', 'Chile']


print(nomesPaises)
print(len(nomesPaises)) #tamanho da lista
print(nomesPaises[0]) #posição 1 da listas
print(nomesPaises[1:3]) #slicing da lista
print("Brasil" in nomesPaises) #verificar se uma string está na lista

# contar quantas vezes um elemento ocorre na lista
x = "Brasil"
c = Counter(nomesPaises) #função conta a quantidade de elementos
print('{} aparece {} vezes na lista.'.format(x, c[x]))

#Adicionar item na lista
nomesPaises.append('Portugal')
print(nomesPaises)

nomesPaises.insert(0,'Russia')
print(nomesPaises)

#Remover item na lista
nomesPaises.remove('Portugal')
print(nomesPaises)

nomesPaises.pop(1)
print(nomesPaises)

#Unpacking  tuplas - extrair valor da tupla e atribuir a variáveis
tuplaPaises = 'Brasil', 'Japão',
America, Asia = tuplaPaises
print(*tuplaPaises) # colocar asterisco remete as variáveis oriundas o unpacking
print(Asia)





