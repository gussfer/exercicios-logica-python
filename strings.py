#Caracter de escape
frase = "Então ele citou: \"pipipi, popopo\""
print(frase)

#Filtrar caracter dentro de strings
print(frase[16:])

#Split - separar strings em listas
nomesPaises = 'Brasil, Brasil, Argentina, Colômbia, Chile'
print(nomesPaises)
listaPaises = nomesPaises.split(', ')
print(listaPaises)

#Formatação de strings
titulo = "   TÍTULO    "
print(titulo)
print(titulo.strip()) #retira espaços na string
    #correção da caixa 
cidade = "rIo dE janEiro"
print(cidade.title())
print(cidade.capitalize())
print(cidade.lower())
print(cidade.upper())
    #EXERCÍCIO
cidadeMaravilhosa = input("Qual cidade do Brasil é conhecida como \"cidade maravilhosa\"?: ")
while cidadeMaravilhosa.lower() != "rio de janeiro":
    print("Tente outra vez!")
    cidadeMaravilhosa = input("Qual cidade do Brasil é conhecida como \"cidade maravilhosa\"?: ")
print("Acertou, miseravi")


