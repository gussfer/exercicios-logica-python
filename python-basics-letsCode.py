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