import random
##

lista01 =random.sample(range(0, 1000), 10)
print(lista01)
print('modificando indice 4')
lista01[4] = 3
print(lista01)
print('adicionando um valor no final da lista')
lista01.append(random.randint(0, 50))
print(lista01)
print('ordenando a lista ')
lista01.sort()
print(lista01)
print('ordem inversa da lista')
lista01.sort(reverse=True)
print(lista01)
print('inserindo elemento no indice 2 e 10')
lista01.insert(2, 0)
lista01.insert(10, 0)
print(lista01)
print('remove o primeiro elemento de valor 0')
lista01.remove(0)
print(lista01)
print('removendo o elemento do indice 3')
lista01.pop(3)
print(lista01)
print(f'Essa lista tem {len(lista01)} elementos.')
##
lista02 = random.sample(range(0, 100), 5)
print(lista02)
for contador, valor in enumerate(lista02):
    print(f'no indice {contador}, encontrei o valor {valor}')
print('FIM')
##
a = random.sample(range(0, 100), 5)
print('criando uma cópia da lista a com o fatiamento :')
b = a[:]
print(f'lista original {a}, cópia {b}')
b[3] = 0
print(f'lista original {a}, cópia modificada {b}')
## DESAFIO 078
''' Faça um proga que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''
def desafio078():
    lista = list()
    for x in range(5):
        lista.append(int(input('digite um valor inteiro')))
    minimo = min(lista)
    maximo = max(lista)
    quantidade = lista.count(minimo)
    quantidade2 = lista.count(maximo)
    print(f'O menor valor digitado foi {minimo}, nas posições:', end=' ')
    for p in range(quantidade):
        posicao = lista.index(minimo)
        print(f'{posicao}', end='... ')
        lista[lista.index(minimo)] = 'removidoMin'
    print(f'\nO maior valor digitado foi {maximo}, nas posições:', end=' ')
    for pm in range(quantidade2):
        posicao = lista.index(maximo)
        print(f'{posicao}', end='... ')
        lista[lista.index(maximo)] = 'removidoMax'
# Resposta professor
listanum = []
mai = 0
men = 0
for c in range(0, 5):  # criar a lista
    listanum.append(int(input(f'digite um valor para posição {c}:')))
    if c == 0:  # descobrir o valor maior e menor
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end=':')

for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {men} nas posições ', end=':')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')

## DESAFIO 079
'''Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já existe 
lá dentro, ele não será adicionado. No final, serão exibidos 
todos os valores únicos digitados, em ordem crescente.'''
valores = []
nun = 1
while nun != 0:
    nun = int(input('digite um valor para adicionar a lista:'))
    if nun in valores:
        print('valor não incluido')
    else:
        valores.append(nun)
        print('digite o valor 0 para parar de adicionar valores:')
valores.sort()
print(valores)

## DESAFIO 080

''' Crie um programa onde o usuário possa digitar cinco valores numéricos
 e cadastre-os em uma lista, ordenados sem usar o sort().'''


def desafio080():
    lista03 = []
    for val in range(5):
        lista03.append(int(input('digite um valor: ')))
    # ordenar a lista
    for i in range(len(lista03) -1):
        for j in range(len(lista03) - i -1):
            if lista03[j] > lista03[j + 1]:
                lista03[j], lista03[j+1] = lista03[j + 1], lista03[j]
    print(lista03)
# Resposta professor
lista = []
for c in range(0, 5):
    n = eval(input('digite um número:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adiconado ao final da lista.')
    else:
        pos = 0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            else:
                pos += 1
print(lista)
## DESAFIO 081

'''Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, mostre:
 A quantos números foram digitados
 B lista de valores ordenadas de forma decrescente
 C se o valor 5 foi digitado e está ou não na lista.'''

valores = []
nun = int(input('digite um valor para adicionar a lista:'))
print('digite o valor 0 para parar de adicionar valores:')
while True:
    if nun == 0:
        break
    valores.append(nun)
    nun = int(input('digite um valor para adicionar a lista:'))
    print('digite o valor 0 para parar de adicionar valores:')
print(f'A - foram digitados {len(valores)}')
valores.sort(reverse=True)
print(f'B - valores ordenados de forma decrescente{valores}')
if 5 in valores:
    print('o valor 5 está na lista')
else:
    print('o valor 5 não está na lista')
##
# Desafio 082
'''Crie um programa que va ler vários números e colocar em uma lista
Depois disso, crie duas listas extras que vão conter apenas os valore pares
eos valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

tamanho = int(input('digite o tamanho da lista:'))
v = []
vpar = []
vimp = []
for x in range(tamanho):
    v.append(int(input('digite um valor:')))
for y in v:
    if y % 2 == 0:
        vpar.append(y)
    else:
        vimp.append(y)
print(f'primeira lista: {v},\n lista par {vpar}\n lista ímpar: {vimp}')
##
# DESAFIO 0 83
'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses,
Seu aplicativo deverá analisar se a expressão passada está com os 
parênteses abertos e fechadas na ordem correta.
'''
'''
# tentativa01
expressa0 = [] # tem um problema com expressões com (2+1(+1(2( 
expressao = input('digite uma expressão:')
quat1 = expressao.count('(')
quat2 = expressao.count(')')
if quat1 == quat2:
    print('expressão válida')
else:
    print('expressão invalida')'''
# Resolução professor

expressao = list(input('digite uma expressão matemática:'))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('expressão válida')
else:
    print('expressão inválida')





