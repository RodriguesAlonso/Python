"""
-------------------------
Decisões de Caminho Único
------------------------

Problema Prático 3.2
Traduza estas instruções condicionais em instruções if do Python:
(a)Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.
(b)Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.
(c)Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
(d)Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.
"""
##
print(" - A - "*5)
idade = eval(input("Digite a idade: "))
if idade > 62:
    print("Você  pode obter o benefício de pensão")
##
print(" - B - "*5)
lista = ['Musial', 'Aaraon', 'William', 'Gehrig', 'Ruth']
nome = input('Digite um nome: ')
if nome in lista:
    print('{} é um dos maiores jogadores de baseball de todos os tempos'.format(nome))
##
print(" - C - "*5)
golpes = eval(input("Digite o numero de golpes:"))
defesa = eval(input("Digite o numero de defesa"))
if golpes > 10 and defesa == 0:
    print('você está morto...')

##
print(" - D - "*5)
direção = input("Digite a direção: ")
if direção == 'norte' or direção == 'sul' or direção == 'leste' or direção == 'oeste':
    print('Posso escapar.')

'''
-------------------------
Decisões de Caminho Duplo
-------------------------
Verifique se três valores, A, B e C pode formar um triângulo.
Se forem, verifique o tipo do triângulo é equilátero, isóscele, escaleno.
'''
##
a = eval(input("digite o valor A: "))
b = eval(input("digite o valor B: "))
c = eval(input("digite o valor C: "))

# maiorLado = max(a, b, c) forma mais rápida de descobrir o maior lado.

lista = [a, b, c]
lista.sort()
lista.reverse()
if lista[0] > lista[1] + lista[2]:
    print("não forma triângulo")
elif a != b and b != c and a != c:
    print('triângulo escaleno')
elif a == b and c == a and b == c:
    print('triângulo equilátero')
else:
    print('triângulo isósceles')

'''
-------------------------
Decisões de Caminho Duplo
-------------------------
Traduza estas declarações em instruções if/else do Python:
(a)Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; 
caso contrário, exiba 'Definitivamente não é um ano bissexto.'
(b)Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez…'.
'''
##
print('-A-'*5)
ano = eval(input('digite o ano:'))
if ano % 4 == 0:
    print('pode ser um ano bissexto')
else:
    print('definitivamente não é um ano bissexto')
##
print('-B-'*5)
contador = 1
lista = []
loteria = [1, 2, 3, 4, 5]
print("digite os números do seu bilhete:")
while contador <= 5:
    x = eval(input('numero {}:'.format(contador)))
    lista.append(x)
    contador += 1
print('seus bilhete: {}'.format(lista))
print('Loteria: {}'.format(loteria))
if lista == loteria:
    print("Você ganhou")
else:
    print('Melhor sorte da próxima vez')
##
'''
Problema Prático 3.4
Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string). 
O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] 
de usuários válidos. Dependendo do resultado, uma mensagem apropriada deverá ser impressa. 
Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar. 

'''
login = input('digite o login: ').lower()
lista = ['joe', 'sue', 'hani', 'sophie']
if login in lista:
    print('Login bem-sucedido')
else:
    print('Usuário inválido')
print('fim')

'''
---------------------
Estruturas de Iteração
----------------------
Problema Prático 3.5
Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e 
depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista.
>>>
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
pare pote
'''
##
lista = list()
contador = 1
while contador < 5:
    item = input("Digite  lista de palavras:").strip()
    lista.append(item)
    contador += 1
for t in lista:
    if len(t) == 4:
        print(t)

'''
Problema Prático 3.6
Escreva o laço for que exibirá as sequências de números a seguir, um por linha, no shell interativo do Python.
(a)Inteiros de 0 a 9 (isto é, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
(b)Inteiros de 0 a 1 (isto é, 0, 1).
'''
##
print('A-'*5)
for i in range(10):
    print(i)

print('B-'*5)
for x in range(2):
    print(x)
'''
Escreva um laço for que exiba a seguinte sequência de números, um por linha.
(a)Inteiros de 3 até 12, inclusive este.
(b)Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto é, 0, 2, 4, 6, 8).
(c)Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.
(d)Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.'''
##
print('<A>'*5)
for a in range(3, 13):
    print(a)
print('<B>'*5)
for b in range(0, 9, 2):
    print(b)
print('<C>'*5)
for c in range(0, 24, 3):
    print(c)
print('<D>'*5)
for d in range(3, 12, 5):
    print(d)
'''
Problema Prático 3.10
Escreva a função negativos(), que aceita uma lista como entrada e 
exibe, um por linha, os valores negativos na lista. A função não deverá retornar nada.'''
##
def negativos (list):
    for x in list:
        if x < 0:
            print(x)

'''
-----------------------
Troca (swapping)
----------------

Problema Prático 3.13
Escreva uma instrução Python ou instruções que mapeiam o primeiro e último valor da lista. Assim, 
se a lista original for:
>>> time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
então a lista resultante deverá ser:
>>> time
['Sarah', 'Eleanor', 'Clare', 'Ava']
'''
##
time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
time[0], time[-1] = time[-1], time[0]
print(time)

'''
Problema Prático 3.14
Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista. 
Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.
>>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
>>> trocaPU(ingredientes)
>>> ingredientes
['maçãs', 'açúcar', 'manteiga', 'farinha']'''
##
ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
def trocaPU(lst):
    lst[0], lst[-1] =lst[-1], lst[0]
