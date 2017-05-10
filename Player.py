# Our players class


class Player(object):
    def __init__(self):
        self.name = "unknown"
        self.alive = True
        self.totalHealth = 10
        self.currentHealth = 10
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

    # The Hero's Attack
    def getAttack(self):
        return self.attack

    # The Hero's Defence
    def getDefense(self):
        return self.defence

    # The Hero's Mortal State
    def isAlive(self):
        return self.alive

    # Resurrect the Hero
    def revive(self):
        self.currentHealth = self.totalHealth
        self.alive = True
