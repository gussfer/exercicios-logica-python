## Algoritmo utilizando 'input' 
n1 = float(input("Insira a nota 1: ")) #necessário conversão de valor str --> int 
n2 = float(input("Insira a nota 2: ")) 
media = (n1+n2)/2

print("A sua média é:", media)

#Estruturas condicionais 
if media >= 6: 
    print("Aprovado") 
else : 
    if media >= 5 and media < 6: 
        print("Exame") 
    else:
        print("Reprovado")

#Estruturas de repetição
# Fazer calculadora while
numero = int(input("Insira o numero para saber a tabuada: "))

i = 1

while i <= 10:
    print(
        "{0} X {1} = ".format(numero, i),
        i * numero
    )
    i = i+1