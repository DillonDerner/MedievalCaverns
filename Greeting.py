# Methods used in the beginning of the game


# Greet the player
def welcome():
    print("|``````````````````````````````|")
    print("| Welcome to Medieval Caverns! |")
    print("|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,|\n")


def namePlayer(player):
    # Name the new player
    player.setName(getPlayerName())


def getPlayerName():
    # Get the players name
    yourName = input('So, who are you?: ')
    print("Hello {},".format(yourName))
    return yourName


def runTutorial():

    showTutorial = str(input("Would you like to view the tutorial(Y/N)?: "))

    if showTutorial == "y":
        print("\n-Tutorial-\n")

        print("To control your character in Medieval Caverns, you will need to ")
        print("enter a command for every turn. Below are the commands available!\n")
        print("To view these commands at any time, type 'help' ")

        # TODO: Add some sort of training tutorial in the future
        helpMenu()


def helpMenu():
    print("1 - Move Ahead")
    print("2 - Move Backwards")
    print("3 - Inventory")
    print("To learn more about a certain command, type help1, help2 or help3")


def help1():
    print("Press '1' to Move Ahead")
    print("Moving ahead is how players progress in Medieval Caverns")
    print("Moving ahead will make the player encounter stronger monsters")


def help2():
    print("Press '2' to Move Backwards")
    print("Moving backwards will allow players to return to previous landmarks")
    print("Players moving backwards will encounter less monsters")
    print("Moving backwards will make the player encounter easier monsters")


def help3():
    print("Press '3' to open your Inventory")
    print("The Inventory shows the player all of the Items they have gathered")
    print("Players who open their inventory have the option to use an Item on that turn")
    print("If a player does not want to use an item, they can simply enter nothing to exit the inventory")
