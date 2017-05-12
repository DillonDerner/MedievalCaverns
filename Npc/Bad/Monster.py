# A basic Enemy class


class Monster(object):
    def __init__(self):
        self.name = None
        self.text = None
        self.totalHealth = None
        self.currentHealth = self.totalHealth
        self.attack = None
        self.defence = None
        self.alive = True

    # Return a string of the monsters Stats
    def getStats(self):
        print("{} | HP:{}/{}| ATK:{} | DEF:{} ".format(self.name,
                                                       self.currentHealth,
                                                       self.totalHealth,
                                                       self.attack,
                                                       self.defence))

    # The name of our Enemy
    def getName(self):
        return self.name

    # The Enemy Dialogue
    def getText(self):
        return self.text

    # The Enemy's HP
    def getHealth(self):
        return self.currentHealth

    # How the Enemy takes damage
    def takeDamage(self, damage):
        if self.currentHealth > damage:
            self.currentHealth = self.currentHealth - damage
        else:
            self.alive = False
        return self.alive

    # The Enemy's Attack
    def getAttack(self):
        return self.attack

    # The Enemy's Defence
    def getDefense(self):
        return self.defence
