import random
import numpy as np
from map import *
from inventory import *

'''The things in the world'''
item_list = [['Treasure Chest', 'Supplies', 1750, 'Ye lucky bastard', 1],
             ['Rum', 'Alcohol', 90, 'What you really came here for', 6],
             ['Leather', 'Textile', 20, 'From cows, maybe?', 30],
             ['Sugar', 'Spice', 3, 'And nice', 250],
             ['Molasses', 'Spice', 6, 'Idk, they probably ate this shit', 70],
             ['Peg-Leg', 'Weapon', 120, 'You\'re going to need it', 4],
             ['Prune O', 'Alcohol', 17, 'They still drink in the brig', 55],
             ['Davey Jones\'s Heart', 'Supplies', 1500, 'The guy from Pirates 3', 1],
             ['Wood', 'Supplies', 10, 'Gotta fix your ship somehow', 90],
             ['Cannonballs', 'Weapon', 45, 'Blow holes in your enemies', 30],
             ['Gunpowder', 'Weapon', 20, 'Gonna need this to blow holes', 20],
             ['Blunderbuss', 'Weapon', 120, 'Fer Shootin', 3],
             ['Dried Fruit', 'Food', 10, 'Keeps the scurvy away', 35],
             ['Pork Bellies', 'Food', 30, 'Pirates loves tacos too', 15],
             ['Wild Onion', 'Spice', 6, 'Idk I needed more items', 30],
             ['Tobacco', 'Spice', 60, 'Smokes, let\'s go.', 15],
             ['Parrot', 'Weapon', 200, 'Annoying piece of gear', 2],
             ['Cannon', 'Weapon', 120, 'For personal home defense', 5],
             ['Eyepatch', 'Textile', 75, 'Cus there be no optometrists', 2],
             ['Sword', 'Weapon', 180, 'Sharp, keep away from children', 7],
             ['Tri-Cornered Hat', 'Supplies', 350, 'Lookin\' good.', 2],
             ['Musket', 'Weapon', 210, 'Business end towards enemy', 3],
             ['Bread', 'Food', 2, 'Wormy, but ya gotta eat', 120],
             ['Mead', 'Alcohol', 20, 'Tastes all right, even when warm.', 40]]

'''The World'''
port_list = [["Tortoise Island", "Buncha turtles, really, all the way down.", 1.1, 0.9, 1.6, .9, .8, 1],
             ["Port Of Rum", "Couple's retreat, I guess", 1.1, 0.9, 1.6, .6, .3, 1],
             ["Atoll Of Dead Whales", "Really sad place, avoid it", 1.05, 1.03, 0.9, 1, .9, .4],
             ["Bay Of Marauders", "Might be Cuba", 1.9, .8, .4, 1, 1.8, 1.3],
             ["Cabo", "I don't remember being here", .4, 1.4, .25, 1, .33, .7],
             ["Galveston", "Did this town even exist then?", .7, .4, 1.8, 1.2, 1.5, 1.5]]


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Plyr_inv(self.name)

    def check_inv(self):
        print("Carrying %.2f pieces of gold" % self.inventory.cash)
        print("And")
        self.inventory.print_items()


class Color:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'


def helper():
    print(Color.bold + Color.green + "You are the Captain of a lone trading ship. \n" 
                                     "Travel around to ports to get yo gold up\n" +
          Color.bold + Color.red + Color.underline + "BASIC CONTROLS: \n" + Color.end +
          Color.bold + Color.cyan +  "-- travel/sail - for going to a new port for a small fee\n"
                                     "-- map - brings up a list of other ports\n"
                                     "-- inventory/inv - see what you have in your hull"
                                     "-- demand/loc/location - see what's for sale in the current port\n"
                                     "-- buy/bid - buy command -> tell them what you want -> how many\n"
                                     "-- sell/ask - sell command -> tell them what you want to sell -> how many\n"
          + Color.end)


def GameLoop(plyr,map):
    running = True
    waiting = True
    cmd = ""
    while (running == True):
        cmd = input("Command: ")
        cmd = cmd.lower()

        if (cmd in ["map","check map", "ports"]):
            map.show_map()
        elif (cmd in ["check demand", "demand", "dmd", "loc", "location", "for sale"]):
            map.curr_port.check_demand()
        elif (cmd in ["inv", "inventory", "stock", "items"]):
            plyr.check_inv()
        elif (cmd in ["go", "travel", "move"]):
            travel(plyr, map, port_list, item_list)
        elif (cmd in ["sell", "ask"]):
            plyr_sells(map.curr_port.inventory, plyr.inventory, item_list)
        elif (cmd in ["buy", "bid"]):
            plyr_buys(map.curr_port.inventory, plyr.inventory, item_list)
        # elif (cmd in ["auto buy","autobuy"]):
        #     auto_buy()
        # elif (cmd in ["auto sell","autosell"]):
        #     auto_sell()
        # utility
        elif (cmd in ["help", "helper"]):
            helper()
        elif (cmd in ["exit","quit"]):
            running = False
        elif (cmd == "clear"):
            for x in range(0, 300):
                print("\n")
        # unknown command
        else:
            print("Unknown Command!")
            print(" ")

def main():
    plyr = Player('jeff')
    game_map = Map(port_list[0], port_list)
    game_map.curr_port.inventory.generate_qty(item_list)

    print(Color.bold + Color.cyan + "Welcome to the Carribbean." + Color.end)
    print(Color.bold + Color.blue + "A terrible trading game made by Jeff D. to practice inventory systems"
          + Color.end)
    helper()
    print(" ")
    GameLoop(plyr,game_map)



if __name__ == '__main__':
    main()
