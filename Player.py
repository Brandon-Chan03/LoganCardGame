import random

class Player:
    def __init__(self, name, deck):
        self._name = name
        self._health = 10
        self._deck = deck

    def getName(self):
        return self._name

    def getHealth(self):
        return self._health

    def getDeck(self):
        return self._deck

    def setHealth(self, amount):
        self._health += amount

    def getRandomCard(self):
        return random.choice(self._deck)
