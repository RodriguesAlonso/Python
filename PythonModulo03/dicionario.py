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
if media >= 7:
    situacao = 'Aprovado'
elif media >= 5:
    situacao = 'em Recuperação'
else:
    situacao = 'Reprovado'
boletim = {'aluno': nome, 'final': media, 'situacao': situacao}
'''print(f'Nome: {boletim["aluno"]}')
print(f'Média de {boletim["aluno"]}: {boletim["final"]}')
print(f'{nome} está {boletim["situacao"]}')'''
# professor
print('-=' * 30)
for v, k in boletim.items():
    print(f'- {v} é igual a {k}')

##
# DESAFIO 91

''' Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número'''
from random import randint
from operator import itemgetter
i = 0
jogadas = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
           'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6),
           'jogador 5': randint(1, 6), 'jogador 6': randint(1, 6)}
for j, v in jogadas.items():
    print(f'{j} jogou {v}')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i +1}º lugar {v[0]} com {v[1]}')






##
# DESAFIO 92
'''Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-os( com idade) em um dicionário
se por acaso a CTPS for diferente de zero, o Dicionario receberá
também o ano de contratação e o salário. Calcule e acrescente, além
da idade, com quantos anos a pessoa vai se aposentar(35 anos de contribuição'''
##
# DESAFIO 93
'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas 
ele jogou. Depois vai ler a quantidade de gols feitos em cada partida
. NO final, tudo isso será guardado em um dicionário, incluindo o total de gols
feito durante o campeonato'''
##
# DESAFIO 94
'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os 
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas 
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média'''
##
# DESAFIO 95
'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.'''
