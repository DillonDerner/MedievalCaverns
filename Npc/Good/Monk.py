# A basic Friendly class

from Npc.Good.Friendly import *


class Monk(Friendly):

    # The name of our Good
    def getName(self):
        return "Monk"

    # The Good Dialogue
    def getText(self):
        return "oOoo Shiny!"
