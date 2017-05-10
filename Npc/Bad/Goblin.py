# A basic Enemy class

from Npc.Bad.Monster import *


class Goblin(Monster):
    def __init__(self):
        self.health = 20

    # The name of our Enemy
    def getName(self):
        return "Goblin"

    # The Enemy Dialogue
    def getText(self):
        return "oOoo Shiny!"

    # The Enemys HP
    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    # The Enemys Attack
    def getAttack(self):
        return 10

    # The Enemys Defence
    def getDefense(self):
        return 1
