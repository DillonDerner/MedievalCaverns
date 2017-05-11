# Create 1st Floor Map

import random

from Variables import *

gameMap = []


# Create a random Game Map
def createMap():

    # Add the map entrance
    gameMap.append(0)

    # Generate Cavern
    for i in range(mapSize - 2):
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
    print("entrance")


def monster(player):
    print("monster")
    print("my attack")
    print(player.getAttack())


def nothing(player):
    print("nothing")


def randomCard(player):
    print("random Card")


def shop(player):
    print("shop")


def cavern(player):
    print("cavern")


def town(player):
    print("town")


def loot(player):
    print("loot")


def bank(player):
    print("bank")


def bigMonster(player):
    print("bigMonster")


def floorBoss(player):
    print("floorBoss")
