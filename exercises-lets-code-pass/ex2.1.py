'''
Faça um programa que leia a validade das informações:
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro;
O programa deve imprimir uma mensagem de erro para cada informação 
inválida
'''
idade = int(input("Informe a idade: "))
while idade <= 0 or idade > 150:
    print("Informe uma idade válida!")
    idade = int(input("Informe a idade: "))
    
salario = int(input("Informe o salário: "))
while salario <= 0:
    print("Informe um salário válido!")
    salario = int(input("Informe o salário: "))

sexo = input("Informe o sexo: ")
while sexo.lower() != "masculino" and sexo.lower() != "feminino" and sexo.lower() != "outro":
    print("Informe um sexo válido!")
    sexo = input("Informe o sexo: ")
