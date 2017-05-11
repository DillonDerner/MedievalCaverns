# A basic Enemy class

from Npc.Bad.Monster import *


class Rat(Monster):
    def __init__(self):
        self.name = "Rat"
        self.text = "Squeak! Squeak!"
        self.totalHealth = 3
        self.currentHealth = self.totalHealth
        self.attack = 1
        self.defence = 1
        self.alive = True
