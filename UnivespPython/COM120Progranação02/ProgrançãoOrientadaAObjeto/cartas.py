##
class Card:
    """Representa uma carta"""

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __eq__(self, other):
        return self.valor == other.valor and self.naipe == other.naipe

    def __repr__(self):
        return "Card('{}','{}')".format(self.valor, self.naipe)

    def getRank(self):
        return self.valor


    def getSuit(self):
        return self.naipe


