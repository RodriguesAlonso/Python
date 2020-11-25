##
presidentes = {
    'Obama': 'hawaii',
    'Bush': 'connecticut',
    'Clinton': 'Arkansas',
    'Bush pai': 'Massachussetts',
    'Reagan': 'Illinois',
    'Carter': 'Georgia'}


def estadoNasc(nome):
    return presidentes[nome]


estadoNasc('Obama')
for z in presidentes:
    x = estadoNasc(z)
    print('o presidente {} nasceu no stado {}'.format(z, x))
##
agenda = {
    '123-321': ['Anna', 'Karenina'],
    '234-432': ['Yu', 'Tsun'],
    '567-765': ['Hans', 'Castorp']}


def look():
    x = input('digiteum número de telefone no formato xxx-xxx')
    print(agenda[x])


##
agenda2 = {
    ('Anna', 'Karenina'): ['123-321'],
    ('Yu', 'Tsun'): ['234-432'],
    ('Hans', 'Castorp'): ['345-543']
}


def look2():
    nome = input('digite o nome:')
    sobrenome = input('digite o sobrenome:')
    nomeCompleto = (nome, sobrenome)
    print(agenda2[nomeCompleto])



##
def contaPalavra(texto):
    y = texto.split()
    print(y)
    contador = {}
    for x in y:
        if x in contador:
            contador[x] += 1
        else:
            contador[x] = 1
    print(contador)
    print(contador['safira'])
    for z in contador:
        print('A palavra {:10} aparece {} vezes'.format(z, contador[z]))


contaPalavra('era uma vez gatinha gatinha bonitinha bonitinha bonitinha que se chama safira safira')
##
dic = {'759147': 54, '186398060': 8, '199846203': 42, '191725321': 10, '158947719': 4}
for item in sorted(dic, key=dic.get):
    print(dic[item])

##
contador = {}
estudantes = ['Cindy', 'John', 'Cindy', 'Adam', 'Adam', 'Jimmy', 'Joan', 'Cindy', 'Joan']
for nome in estudantes:
    if nome in contador:
        contador[nome] += 1
    else:
        contador[nome] = 1
print(contador)
##
