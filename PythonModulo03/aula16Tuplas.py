lanches = 'hamburgue', 'suco', 'pizza', 'pudin'
#tuplas são imutáeis
##
for comida in lanches:
    print(f'hoje eu comi {comida}')

for c in range(0, len(lanches)):
    print(f'eu comi {lanches[c]}')

for pos, comida in enumerate(lanches):
    print(f'eu vou comer {comida} na posição {pos}')
##
a = 2, 5, 4
b = 5, 8, 1, 2
c = a + b
print(c)
print(len(c))
print(sorted(c))
print(c.count(2))
print(c.index(2))
for contador in c:
    print("contador", contador, ":", c.count(contador))
for posicao in c:
    print('posição', posicao, "na posição:", c.index(posicao))
## DESAFIO 072
def tuplaEx():
    try:
        tupla = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
        numero = int(input('digite um número de 0 até 10: '))
        if numero>=0:
            print(f'{numero} por extenso é {tupla[numero]}')
        else:
            print('digitou número inválido')
            tuplaEx()
    except:
        print('digitou número inválido')
        tuplaEx()
    continuar = input('digite sim para continuar:').lower().strip()
    if continuar == 'sim':
        tuplaEx()
    else:
        print('Fim do programa')
## DESAFIO 073
    comida = 'hamburgue', 'arroz', 'feijão', 'palmito', 'banana', 'alfase', 'chocolate', 'macarrão', 'bifão'\
        , 'hot dog','coca-cola'
    print(f'primeiras cinco comidas {comida[0:6]}')
    print(f'4 últimas comidas {comida[-4:]}')
    print(f'lista de comidas em ordem {sorted(comida)}')
    print(f'a banana está na posição: {comida.index("banana") + 1}')

## DESAFIO 074
from random import randint
t = randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100)
print(t)
print(f'o menor é {min(t)} e o maior é {max(t)}')

## DESAFIO 075
#Gambiarra:
'''i = [] 
for x in range(4):
    n = eval(input('digite um número: '))
    i.append(n)
t = (i[0], i[1], i[2], i[3])
print(type(t))
print(t)
'''
# sem gambiarra:
t = (
    (int(input('digite um número:'))),
    (int(input('digite um número:'))),
    (int(input('digite um número:'))),
    (int(input('digite um número:'))))

print(type(t))
print(t)
print(f'o número 9 aprece {t.count(9)} vezes')
try:
    print(f'o valor 3 aparece na posição {t.index(3) + 1}')
except:
    print('a tupla não possui o valor 3')
for par in t:
    if par % 2 == 0:
        print(par, end=',')
print('são pares')
## DESAFIO 076
i = 0
comida = 'hamburgue', 10.5, 'arroz', 20, 'feijão', 300.50, 'palmito', 4, 'banana', 5

'''for x in range(int(len(comida)/2)):
    print(comida[i], end='.'*(20 -(len(comida[i]))))
    print('R$:', comida[i+1])
    i += 2'''
#solução professor
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(comida)):
    if pos % 2 == 0:
        print(f'{comida[pos]:.<30}', end='')
    else:
        print(f'R${comida[pos]:>7.2f}')
print('-'*40)
## DESAFIO 077



comida = 'hamburgue', 'arroz', 'feijão', 'palmito', 'banana', 'alfase', 'chocolate', 'macarrão', 'bifão'\
        , 'hot dog','coca-cola'
''' Muitos IFs
def maior(y):
    return y > 0
for x in comida:
    print(f'\nNa palavra {x.upper()} temos: ',end=' ')
    a = x.count('a')
    if maior(a):
        print('a '*a, end='')
    e = x.count('e')
    if maior(e):
        print('e '*e, end='')
    i = x.count('i')
    if maior(i):
        print('i '*i, end='')
    o = x.count('o')
    if maior(o):
        print('o '*o, end='')
    u = x.count('u')
    if maior(u):
        print('u '*u, end='')
    contagem = [a, e, i, o, u]'''

for p in comida:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letras in p:
        if letras in 'aeiou':
            print(f'{letras.lower()}', end=' ')



