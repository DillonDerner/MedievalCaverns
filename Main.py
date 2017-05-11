# Medieval Caverns
# Dillon Derner

from Player import *
from Turn import *
from Map import *


def Main():
    welcome()

    # Create the new player
    player = Player()

    # Create the new map
    theMap = createMap()

    if showExtras:
        print(theMap)

    if tutorial:
        namePlayer(player)
        runTutorial()

    print()
    while player.alive:
        Turn(player, theMap)


Main()
