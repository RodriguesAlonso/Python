##
class Point:
    'classe que representa um ponto'

    def __init__(self, coordx=0, coordy=0):
        self.x = coordx
        self.y = coordy

    def __repr__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def setx(self, coordx):
        self.x = coordx

    def sety(self, coordy):
        self.y = coordy

    def getx(self):
        return self.x

    def get(self):
        return self.x, self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class Vetor(Point):

    def __repr__(self):
        return 'Vetor {}'.format(self.get())

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)


##
class Animal:

    def __init__(self, especie='animal', linguagem='sons'):
        self.especie = especie
        self.linguagem = linguagem

    def setEspecie(self, nome):
        self.especie = nome

    def setLinguagem(self, lingua):
        self.linguagem = lingua

    def speak(self):
        print('Eu sou um {} e digo {}'.format(self.especie, self.linguagem))


class Ave(Animal):

    def speak(self):
        print('{}!'.format(self.linguagem * 3))


##
class Retangulo:

    def setTamanho(self, larg, compri):
        self.l = larg
        self.c = compri

    def perimetro(self):
        x = self.l
        y = self.c
        print((x + y) * 2)

    def area(self):
        x = self.l
        y = self.c
        print(x * y)


##
class EmptyQueueError(Exception):
    pass


class Queue:

    def __init__(self, fila=None):
        if fila is None:
            self.fila = []
        else:
            self.fila = fila

    def enqueue(self, item):
        self.fila.append(item)

    def dequeue(self):
        try:
            return self.fila.pop(0)
        except:
            print('fim da fila')

    def isempty(self):
        return len(self.fila) == 0

    def __len__(self):
        return len(self.fila)

    def __repr__(self):
        return 'Queue({})'.format(self.fila)

    def __eq__(self, other):
        return self.fila == other.fila


class Queue2(list):

    def enqueue(self, item):
        return self.append(item)

    def dequeue(self):
        if len(self) == 0:
            raise EmptyQueueError('fila vazia')
        return self.pop(0)

    def isempty(self):
        return len(self) == 0


##
from random import shuffle


class Card:
    """Representa uma carta"""

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def getrank(self):
        return self.valor

    def gets1uit(self):
        return self.naipe


##
class Baralho:
    """baralho com 52 cartas"""

    # valores e naipes são variáveis da classe Baralho
    valores = {'2', '3', '4', '5', '6', '7', '8', '10', 'J', 'Q', 'K', 'A'}

    # naipes são 4 símbolos Unicode representado os 4 naipes
    naipe = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self, listacarta=None):
        if listacarta != None:
            self.baralho = listacarta
        else:
            """inicializa baralho de 52 cartas"""
            self.cartas = []
            self.baralho = []  # baralho inicial vazio
            for naipe in Baralho.naipe:  # Naipes e valores
                for valor in Baralho.valores:  # variáveis da classe
                    self.baralho.append([valor, naipe])  # incluir Carta com certo valor e naipe

    def sfuffle(self):
        """misturar o baralho"""
        shuffle(self.baralho)

    def distribuircarta(self):
        """distribui (remove e retorna) carta do topo do baralho"""
        return self.baralho.pop()

    def __len__(self):
        return len(self.baralho)

    def __repr__(self):
        return 'Baralho({})'.format(self.baralho)

    def __eq__(self, other):
        return self.baralho == other.baralho


##
import random


class MinhaLista(list):
    def escolha(self):
        return random.choice(self)


##
class Funcionario:

    def __init__(self, nome=None, data=None, salario=None):
        self.nome = nome
        self.data = data
        self.salario = salario

    def __repr__(self):
        return 'O funcionário {} foi admitido em {}, seu salário é de:R${}'.format(self.nome, self.data, self.salario)

    def setnome(self, nome):
        self.nome = nome

    def setdata(self, data):
        self.data = data

    def setsalario(self, salario):
        self.salario = salario

    def getfuncionario(self):
        return 'O funcionário {} foi admitido em {}, seu salário é de:R${}'.format(self.nome, self.data, self.salario)


class Gerente(Funcionario):

    def setbonus(self, bonus):
        self.bonus = bonus

    def getfuncionario(self):
        return 'O funcinário {} foi admitido em {}, seu salário é de R$:{}, ' \
               'mais o bonus de R$:{}'.format(self.nome, self.data, self.salario, self.bonus)


class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):
        return not len(self.data) > 0


class Fila:
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0


class P:
    def __init__(self, nome, idade):
        self.n = nome
        self.i = idade

    def __repr__(self):
        return '{} tem {} anos'.format(self.n, self.i)

    def setNome(self, x):
        self.n = x

    def setIdade(self, y):
        self.i = y

    def idade(self):
        return self.i

    def nome(self):
        return self.n


class Banco:
    def __init__(self):
        self.filaNormal = []
        self.filaPrioritaria = []

    def fila(self, p):
        if p.idade() <= 60:
            self.filaNormal.append(p.nome())
        else:
            self.filaPrioritaria.append(p.nome())

    def fnormal(self):
        return self.filaNormal

    def fprioritaria(self):
        return self.filaPrioritaria

    def remove(self):
        if len(self.filaPrioritaria) > 0:
            self.filaPrioritaria.pop(0)
            self.filaPrioritaria.pop(0)
            if len(self.filaNormal) > 0:
                self.filaNormal.pop(0)




