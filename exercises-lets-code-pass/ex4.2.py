'''
Crie um dicionário cujas chaves são os meses do ano e os valores são a duração (em dias) de cada mês.
'''

calendario = {
    'Janeiro': 31,
    'Fevereiro': 28,
    'Março' : 31,
    'Abril': 30,
    'Maio': 31,
    'Junho': 30,
    'Julho': 31,
    'Agosto': 31,
    'Setembro': 30,
    'Outubro': 31,
    'Novembro': 30,
    'Dezembro': 31,
}
#utilizando for para imprimir

for mes, dias in calendario.items():
    print("{} - {}".format(mes, dias))
