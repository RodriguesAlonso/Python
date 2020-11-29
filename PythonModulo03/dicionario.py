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
##
# DESAFIO 90
'''Faça um programa que leia nome e média de um aluno
, guardando também a situação. no final mostre o conteúdo da
estrutura na tela'''

boletim = {}
nome = input('Digite o nome: ')
media = eval(input(f'Digite a média de {nome}:'))
if media > 5:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
boletim = {'aluno': nome, 'final': media, 'situacao': situacao}
print(f'Nome: {boletim["aluno"]}')
print(f'Média de {boletim["aluno"]}: {boletim["final"]}')
print(f'{nome} está {boletim["situacao"]}')

##
# DESAFIO 91

''' Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número'''

from random import randint

##
# DESAFIO 92
'''Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-os( com idade) em um dicionário
se por acaso a CTPS for diferente de zero, o Dicionario receberá
também o ano de contratação e o salário. Calcule e acrescente, além
da idade, com quantos anos a pessoa vai se aposentar'''
##
# DESAFIO 93
##
# DESAFIO 94
##
# DESAFIO 95
