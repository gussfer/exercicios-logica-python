'''
4) Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.
'''
# Fazer calculadora while
numero = int(input("Insira o numero para saber a tabuada: "))

i = 1

while i <= 10:
    print(
        "{0} X {1} = ".format(numero, i),
        i * numero
    )
    i += 1