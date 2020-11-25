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
