# The logic behind what will happen when a player enters a command

from Greeting import *

# Lists of all possible input
moveAheadList = ["1", "move ahead", "ahead", "a"]
moveBackwardsList = ["2", "move backwards", "backward", "b"]
moveInventoryList = ["3", "invent", "inventory", "i", "backpack"]
moveHelpList = ["help", "help1", "help2", "help3"]


def Turn(player):
    player.getStats()
    move = str(input("What shall you do?: ")).lower()

    print()
    if move in moveAheadList:
        MoveAhead()
    elif move in moveBackwardsList:
        MoveBackwards()
    elif move in moveInventoryList:
        AccessInventory()
    elif move in moveHelpList:
        options = {
            "help": helpMenu,
            "help1": help1,
            "help2": help2,
            "help3": help3}
        options[move]()
    else:
        DisplayHelp()

    Turn(player)


def MoveAhead():
    print("Moved Forward")
    # enemy1 = Goblin()
    # enemy2 = Goblin()
    # enemy2.setHealth("10")
    # print("a hostile ")
    # print(enemy1.getName())
    # print(enemy2.getHealth())
    # print("approaches")


def MoveBackwards():
    print("Moved Backward")


def AccessInventory():
    print("AccessedInventory")


def DisplayHelp():
    print("Not a vaild command, try one of these...")
    helpMenu()
    print()
