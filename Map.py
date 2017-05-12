# Create 1st Floor Map

import random
from Variables import *

from Npc.Bad.Rat import *
from Npc.Bad.Goblin import *


gameMap = []


# Create a random Game Map
def createMap():

    # Add the map entrance
    gameMap.append(0)

    # Generate Cavern
    for i in range(mapSize - 2):

        # Create the density of monster encounters
        if random.randint(1,100) < monsterDensity:
            gameMap.append(1)

        # Add random tiles
        else:
            gameMap.append(random.randint(1, 9))

    # Add the Boss Room
    gameMap.append(10)

    return gameMap


# Pass the player then run the map tile they are on
def encounter(player, theMap):
    number = theMap[player.getLocation()]
    tile = {
        0: entrance,
        1: monster,
        2: nothing,
        3: randomCard,
        4: shop,
        5: cavern,
        6: town,
        7: loot,
        8: bank,
        9: bigMonster,
       10: floorBoss}
    tile[number](player)


def entrance(player):
    print("{} is at the entrance! Move Ahead!".format(player.getName()))


def monster(player):
    print("monster")

    monsters = {
        0: Rat,
        1: Goblin}

    print(len(monsters))
    randomNumber = random.randint(0, len(monsters)-1)
    randomMonster = monsters[randomNumber]()

    # show the monsters stats
    randomMonster.getStats()

    # TODO Add a combat system

    print("my attack")
    print(player.getAttack())

    # TODO Add a reward system


def nothing(player):
    print("You didn't find anything interesting here...")
    # TODO Add a funny random messages that have to do with 'nothing'

def randomCard(player):
    print("random Card")
    # TODO Add the random reward card system

def shop(player):
    print("shop")


def cavern(player):
    print("{} has found a mysterious cavern!".format(player.getName()))
    enterCavern = str(input("Would you like to see where it leads? (Y/N): ")).lower()

    if enterCavern in yes:
        direction = random.randint(1, 2)

        # TODO Add a reward system

        if direction == 1:
            print("The cavern lead you forward!")
            player.moveLocation(10)

        else:
            print("The cavern lead you backward!")
            player.moveLocation(-10)

        print()
        encounter(player, gameMap)

    else:
        print("You did not enter the cavern.")

def town(player):
    print("town")
    # TODO Add different buildings to visit


def loot(player):
    randomMoney = random.randint(10, player.getCombatLevel() * 2)
    print("{} found ${}!".format(player.getName(), randomMoney))
    player.addMoney(randomMoney)

    # TODO Add a reward system


def bank(player):
    print("You found a Bank!")
    print("|-_-_-| {}'s BANK VALUE: ${} |-_-_-|".format(player.getName(), player.getBankValue()))
    print()  # aesthetic space

    useBank = str(input("Would you like to use the Bank?(Y/N): ")).lower()
    print()  # aesthetic space

    if useBank in yes:
        print("To withdraw money, type \"W\"")
        print("To deposit money,  type \"D\"")
        print("To leave the bank, type \"L\"")
        bankAction = str(input()).lower()

        while bankAction != "l":
            print()  # aesthetic space

            # Withdraw
            if bankAction in ["w", "withdraw"]:
                # prompt the player for an amount
                amount = str(input("How much would you like to withdraw?: $"))

                # check to make sure that the amount entered is a number
                if not amount.isnumeric():
                    print("Please enter a number!")

                # convert to int
                else:
                    # do the transaction
                    amount = int(amount)
                    player.withdrawFromBank(amount)

            # Deposit
            elif bankAction in ["d", "deposit"]:
                # prompt the player for an amount
                amount = str(input("How much would you like to deposit?: $"))

                # check to make sure that the amount entered is a number
                if not amount.isnumeric():
                    print("Please enter a number!")

                # convert to int
                else:
                    # do the transaction
                    amount = int(amount)
                    player.addToBank(amount)

            # Bad Input Response
            else:
                print("Please type "
                      "(\"W\" to withdraw money), "
                      "(\"D\" to deposit money) or "
                      "(\"L\" to leave the bank.): ")

            print()  # aesthetic space
            print("-_-_-| {}'s BANK VALUE: ${} |-_-_-".format(player.getName(), player.getBankValue()))
            bankAction = str(input("What would you like to do?(W/D/L): ")).lower()

        print("Thank you for using our bank!")

    else:
        print("You did not use the bank.")

def bigMonster(player):
    print("bigMonster")
    # TODO Add a reward system

def floorBoss(player):
    print("floorBoss")
    # TODO Add a reward system
    # TODO Add a next floor system