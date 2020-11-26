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
for peso in pessoas:
    if len(dado) == 0:
        dado.append(peso)
    else:
        if peso[1] >= dado[1]:
            maior.insert(0, peso)
        else:
            if peso[1] <= dado[1]:
                menor.insert(0, peso)


print(f'O maior peso foi {maior[0]}. Peso de {maior[1]}')
print(f'O menor peso foi {menor[0]}. Peso de {menor[1]}')


