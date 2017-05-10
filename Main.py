# Medieval Caverns
# Dillon Derner

from Npc.Bad.Goblin import *
from Greeting import *
from Player import *
from Turn import *

# Set this to True to play the full game / False to debug
fullMode = False
tutorial = False


def Main():
    welcome()

    # Create the new player
    player = Player()

    if fullMode:
        namePlayer(player)
    if tutorial:
        runTutorial()

    print()
    Turn(player)


Main()
