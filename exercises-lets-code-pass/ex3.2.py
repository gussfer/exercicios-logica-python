'''
3.2) Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].
'''
import random
# def geraLista():
#     listaNumeros = random.sample(range(10),3) #gerar uma lista aleatória
#     print(listaNumeros)
#     listaNumeros2 = random.sample(range(10),3) #gerar uma lista aleatória
#     print(listaNumeros2)
#     novalista = [listaNumeros[0]+listaNumeros2[0], listaNumeros[1]+listaNumeros2[1], listaNumeros[2]+listaNumeros2[2]]
#     return  "[{}+{}, {}+{}, {}+{}] = {} ".format(listaNumeros[0],listaNumeros2[0],listaNumeros[1],listaNumeros2[1],listaNumeros[2],listaNumeros2[2], novalista )
# print(geraLista())

#modo alternativo
def somaListas(a,b):
    novalista = []
    for x in range(len(a)):
        novalista.append(a[x]+b[x])
    return  "[{}+{}, {}+{}, {}+{}] = {} ".format(a[0],b[0],a[1],b[1],a[2],b[2], novalista )

listaNumeros = random.sample(range(10),3) #gerar uma lista aleatória
print(listaNumeros)
listaNumeros2 = random.sample(range(10),3) #gerar uma lista aleatória
print(listaNumeros2)
#chamando a função
print(somaListas(listaNumeros,listaNumeros2 ))