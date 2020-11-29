# Teoria
pessoas = {'nome': 'João', 'Sexo': 'M', 'idade': 32}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print('metodo key', pessoas.keys())
print('metodo values', pessoas.values())
print('metodo items', pessoas.items())
for k, v in pessoas.items():
    print(f'{k}, {v}')
##
brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['sigla'])
##
estado = {}
brasil = []
for c in range(3):
    estado['uf'] = str(input('Unidade Fedreativa: '))
    estado['sigla'] = str(input('Sliga do Estado'))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()