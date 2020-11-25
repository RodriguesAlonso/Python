
##

agenda1 = {'123', '456', '789'}
agenda2 = {'123', '222', '789'}
agenda3 = {'333', '456', '789'}
agendas = [agenda1, agenda3, agenda2]


def sync(agendas):
    agenda = set()
    for lista in agendas:
        agenda = agenda | lista
    return agenda
print(sync(agendas))
##


def codifica(frase):
    print('char decimal hex binário')
    for char in frase:
        codi = ord(char)
        print('{}\t {:7}\t {:4x}\t {:7b}'.format(char, codi, codi, codi))
##


def chares(ini, fim):
    for letra in range(ini, fim+1):
        print(chr(letra))

##
import random


def adivinhe(numero):
    x = random.randrange(0, numero)
    n = -1
    while n != x:
        n = int(input('Digite seu número:'))
        if n < x:
            print('Muito baixo.')
        elif n > x:
            print('Muito alto.')

    print('Acertou!')
##




