# A basic Enemy class

from Npc.Bad.Monster import *


class Goblin(Monster):
    def __init__(self):
        self.name = "Goblin"
        self.text = "oOoo Shiny!"
        self.totalHealth = 10
        self.currentHealth = self.totalHealth
        self.attack = 1
        self.defence = 1
        self.alive = True
