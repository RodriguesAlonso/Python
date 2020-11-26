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
maior = menor = pesos = list()
i = 0

for p in range(tamanho):
    dado.append(input('Nome:'))
    dado.append(int(input('Peso:')))
    pessoas.append(dado[:])
    dado.clear()
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
i = 0
for peso in pessoas:
    dado.append(peso)
    if peso[0][1] >= peso[i]:
        dado[0][0].insert(-1, peso)
    else:
        if peso[1][0] <= dado[1]:
            dado.insert(0, peso)
i +=1
print(dado)

print(f'O maior peso foi {maior[0]}. Peso de {maior[1]}')
print(f'O menor peso foi {menor[0]}. Peso de {menor[1]}')

##
# DESAFIO 85
'''Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostra os valores pares e ímpares em ordem crescente'''

numeros = list()
numeros.append([0])
numeros.append([0])
print(numeros)
for x in range(1, 8):
    y = int(input(f"digite o valor {x}o. valor: "))
    if y % 2 == 0:
        numeros[0].append(y)
    else:
        numeros[1].append(y)
numeros[0].pop(0)
numeros[1].pop(0)
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
        n = int(input(f'digite o valor da linha {linha} e colina {coluna}:'))
        matriz[linha][coluna] = n
print(matriz)
l = 0
c = 0
for f in range(3):
    print('-' * 3)
    for f2 in range(2):
        print(f'---\n|{matriz[f][f2]}|',end='')



