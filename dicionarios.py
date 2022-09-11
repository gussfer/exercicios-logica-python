#Coleção associativa não relacionada - par chave valor
dadosCidade = {
    'Nome': 'São Paulo',
    'Estado': 'São Paulo',
    'Área (km²)' : 1521,
    'População (milhões)': 12.18
}
print(dadosCidade)
#Adicionar item
dadosCidade['País'] = 'Brasil'
print(dadosCidade)

#Atalizar dicionários
novosDados = {
    'População (milhões)': 15.00,
    'Fundação': '25/01/1554'
}
dadosCidade.update(novosDados)
print(dadosCidade)