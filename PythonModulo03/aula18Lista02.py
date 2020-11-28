##
# teoria
teste = list()
galera = list()
teste.append('João')
teste.append(32)
galera.append(teste[:])  # criando cópia da lista teste
teste[0] = 'bel'
teste[1] = '34'
galera.append(teste[:])
print(galera)
##
galera = list()
dado = list()
totmai = totmem = 0
for c in range(0,3):  # guarda na lista dado o nome e a idade digitados
    dado.append(input('Nome:'))
    dado.append(int(input('Idade:')))
    galera.append(dado[:]) # copia os dados para a lista galera
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:  # conta o número de pessoas maior de idade
        print(f'{p[1]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')  # conta o número de pessoas menor de idade
        totmem += 1
print(f'Temos o tatal de {totmai} pessoas maiores idade')
print(f'Temos o total de {totmem} pessoas menores de idade')

##
# Desafio084

'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
A) Quantas pessosa foram cadasatradas.
B) Uma listagem com as pessoas mais pesadas 
C) Uma listagem com as pessoas mais leves'''

tamanho = int(input('Digite o tamanho de pessoas a ser cadastrado:'))
dado = list()
pessoas = list()
maior = menor = 0
for p in range(tamanho):
    dado.append(input('Nome:'))
    dado.append(float(input('Peso:')))
    if len(pessoas) == 0:
        maior = dado[1]
        menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=', ')
print(f'\nO menor peso foi {menor}', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=', ')
##
# DESAFIO 85
'''Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostra os valores pares e ímpares em ordem crescente'''

numeros = [[], []]
print(numeros)
for x in range(1, 8):
    y = int(input(f"digite o valor {x}o. valor: "))
    if y % 2 == 0:
        numeros[0].append(y)
    else:
        numeros[1].append(y)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}')
print(f'Os valores ímpares foram: {numeros[1]}')

##
# DESAFIO 86
'''Crie um programa que crie uma matriz de dimensão 3x3 r
preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta'''

matriz = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite o valor da linha {linha} e colina {coluna}:'))
for f in range(3):
    for f2 in range(3):
        print(f'[{matriz[f][f2]:^5}]', end='')
    print('')
##
# DESAFIO087
'''Aprimore o desafio anterior. mostrando no final:
A) A soma de todos os valores pares.
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha'''

matriz = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite o valor da linha {linha} e colina {coluna}:'))
for f in range(3):
    for f2 in range(3):
        print(f'[{matriz[f][f2]:^5}]', end='')
    print('')
somapar = 0
somatres = 0
maiorvalor = max(matriz[1])
for p in matriz:
    for c in p:
        if c % 2 == 0:
            somapar += c
print(f'\nA soma dos numeros pares: {somapar}')
for p in range(0, 3):
    somatres += matriz[p][2]
print(f'A soma dos dos valore da terceira coluna: {somatres}')
print(f'O maior valor da segunda linha é {maiorvalor}')
##
# DESAFIO 88
'''Faça um programa que ajude um jogador da MEGASENA a criar
palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
def jogos(tamanho):
    from random import randint
    # tamanho = int(input('Quantos jogos serão gerados? '))
    for j in range(tamanho):
        jogos = list()
        i = 0
        for j in range(6):
            jogos.append(randint(1, 60))
            print(jogos)
            c = jogos.count(jogos[i])
            while c > 1:
                jogos[i] = randint(1, 60)
                c = jogos.count(jogos[i])
            i += 1

        print(jogos)
# resposta professor
from random import randint
from time import sleep
tamanho = int(input('quantos jogos criar ? '))
ljogo = []
totaljogos = []
c = 1
for j in range(tamanho):
    while c <= 6:
        num = randint(1, 60)
        if num not in ljogo:
            ljogo.append(num)
        c += 1
    totaljogos.append(ljogo[:])
    ljogo.clear()
    c = 0
print('-='*3, f'SORTEANDO {tamanho} JOGOS','-='*3)
for i, l in enumerate(totaljogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)

##
# DESAFIO 89
'''Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. no final, mostre 
um boletim contendo a média de cada um e permita 
que o usuário possa mostrar as notas de 
cada aluno individualmente'''

boletim = []
dado = []
for n in range(2):
    dado.append(n)
    dado.append(input('Nome:'))
    dado.append(input('nota 1:'))
    dado.append(input('nota 2:'))
    media = (int(dado[2]) + int(dado[3])) / 2
    dado.append(media)
    boletim.append(dado[:])
    dado.clear()
print(boletim)
print('-=' * 30)
print(f'{"No.":4<} {"NOME":<10}  {"MÉDIA":>8}')
print('-' * 26)
i = 0
while i <= len(boletim[0][1]):
    print(f'{boletim[i][0]:<4}{boletim[i][1]:<10}{boletim[i][2]:>8}')
    i += 1
while True:
    n = int(input('Digite o número do aluno para ver as notas:'))
    print(f'Notas de {boletim[n][1]} são: {boletim[n][2:4]}')
    x = input('quer consultar a nota de outro aluno: [S]/[N]')
    if x in 'nN':
        break
print('fim')
