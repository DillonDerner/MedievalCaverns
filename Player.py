# Our players class

from Variables import *


class Player(object):
    def __init__(self):
        self.name = "unknown"
        self.alive = True
        self.totalHealth = 10
        self.currentHealth = 10
        self.location = -1
        self.attack = 1
        self.defence = 1
        self.money = 0
        self.deaths = 0

    # The name of our Hero
    def getName(self):
        return self.name

    # Name the Hero
    def setName(self, name):
        self.name = name

    # Return a string of the players Stats
    def getStats(self):
        print("{} | HP:{}/{}| ATK:{} | DEF:{} | ${}".format(self.name,
                                                            self.currentHealth,
                                                            self.totalHealth,
                                                            self.attack,
                                                            self.defence,
                                                            self.money))

    # The Hero's HP lvl
    def getTotalHealth(self):
        return self.totalHealth

    # Increase the Hero's HP
    def increaseTotalHealth(self, health):
        self.totalHealth = self.totalHealth + health
        self.currentHealth = self.currentHealth + health

    # The Hero's current HP
    def getCurrentHealth(self):
        return self.currentHealth

    # How the Hero takes damage
    def takeDamage(self, damage):
        if self.currentHealth > damage:
            self.currentHealth = self.currentHealth - damage
        else:
            self.alive = False
        return self.alive

    # How strong the Hero is
    def getCombatLevel(self):
        combatLevel = self.totalHealth + self.attack + self.defence
        return combatLevel

    # The Hero's location on the game board
    def getLocation(self):
        return self.location

    # Move the Hero's location on the game board
    def moveLocation(self, distance):
        # Do not let the user go to a negative location
        if (self.location + distance) <= 0:
            self.location = 0

        # Do not let the user exceed the map bounds
        elif (self.location + distance) > mapSize - 1:
            self.location = mapSize - 1

        # Move the user within the map
        else:
            self.location = self.location + distance

    # The Hero's Attack
    def getAttack(self):
        return self.attack

    # The Hero's Defence
    def getDefense(self):
        return self.defence

    # Resurrect the Hero
    def revive(self):
        self.currentHealth = self.totalHealth
        self.alive = True
        # reset location?
