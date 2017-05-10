# A basic Enemy class


class Monster(object):

    # The name of our Enemy
    def getName(self):
        raise NotImplementedError  # you want to override this on the child classes

    # The Enemy Dialogue
    def getText(self):
        raise NotImplementedError  # you want to override this on the child classes

    # The Enemy's HP
    def getHealth(self):
        raise NotImplementedError  # you want to override this on the child classes

    # The Enemy's Attack
    def getAttack(self):
        raise NotImplementedError  # you want to override this on the child classes

    # The Enemy's Defence
    def getDefense(self):
        raise NotImplementedError  # you want to override this on the child classes

