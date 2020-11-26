print('algo')

##
def par(x):  # função identifica par ou impar
    if x % 2 == 0:
        print(f'{x} é par')
    else:
        print(f'{x} é impar')


def lisA(tamanho, alcance):  # Cria listas aleatórias
    from random import randint
    lista = []
    for x in range(tamanho):
        lista.append(randint(0, alcance))
    return lista
