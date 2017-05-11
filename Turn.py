# The logic behind what will happen when a player enters a command

from Variables import *
from Greeting import *
from Map import *
import random

# Lists of all possible input
moveAheadList = ["1", "move ahead", "ahead", "a"]
moveBackwardsList = ["2", "move backwards", "backward", "b"]
moveInventoryList = ["3", "invent", "inventory", "i", "backpack"]
moveHelpList = ["help", "help1", "help2", "help3"]


def Turn(player, theMap):
    player.getStats()
    move = str(input("What shall you do?: ")).lower()
    print()

    if move in moveAheadList:
        MoveAhead(player, theMap)

    elif move in moveBackwardsList:
        MoveBackwards(player, theMap)

    elif move in moveInventoryList:
        AccessInventory(player)

    elif move in moveHelpList:
        options = {
            "help": helpMenu,
            "help1": help1,
            "help2": help2,
            "help3": help3}
        options[move]()

    else:
        DisplayHelp()

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  \n")


def MoveAhead(player, theMap):
    print("{} moved ahead...\n".format(player.getName()))

    # Decide a random amount of distance to travel 1-6(dice)
    distance = random.randint(1, 6)
    if showExtras:
        print("rolled: " + str(distance))

    # Update the players current location
    player.moveLocation(distance)
    if showExtras:
        print("Map Location: " + str(player.getLocation() + 1))

    # Figure out where the player landed
    encounter(player, theMap)

    #TODO Add a random encounter system

    #TODO Add a reward system




def MoveBackwards(player, theMap):
    print("{} moved backward...\n".format(player.getName()))

    # Decide a random amount of distance to travel 1-3
    distance = random.randint(-3, -1)
    if showExtras:
        print("rolled: " + str(distance))

    # Update the players current location
    player.moveLocation(distance)
    if showExtras:
        print("Map Location: " + str(player.getLocation() + 1))

    # Figure out where the player landed
    encounter(player, theMap)


def AccessInventory():
    print("Accessed Inventory\n")


def DisplayHelp():
    print("Not a vaild command, try one of these...")
    helpMenu()
    print()
