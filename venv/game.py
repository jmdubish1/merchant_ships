import random
import numpy as np
from map import *
from inventory import *

'''The drugs in the world'''
drug_list = [['Wheeze', 'Downer', 20, 'The chronic, the good shit. Classic', 50],
             ['Stimpak', 'Painkiller', 50, 'Keeps you going through the show', 40],
             ['Jet', 'Upper', 25, 'better than cocaine', 55],
             ['Kram', 'Upper', 35, 'doinky doinky', 50],
             ['Lsx', 'Painkiller', 5, 'Bad drug man', 100],
             ['Prune-o', 'Downer', 3, 'Made in China', 90],
             ['The-Best', 'Upper', 95, 'No one really knows what it is', 10]]

'''The World'''
city_list = [["Victory", "description", 1.1, 0.9],
             ["Arrival", "description"],
             ["Boost", "description", 1.05, 1.03, 0.9]]


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Plyr_inv(self.name)

    def check_inv(self):
        print("Carrying $$%s" % self.inventory.cash)
        print("And")
        self.inventory.print_items()


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def helper():
    print(Color.BOLD + Color.GREEN + "BASIC COMMANDS: \ntravel - Go to a new place (costs some money)\nmap - "
                                     "Check your map\nlocation - Info about your current location\ninv - Check your "
                                     "stock\ndemand - Check the price of drugs in your current location\nbuy - "
                                     "Buy drugs\nsell - Sell Drugs " + Color.END)


def GameLoop(p1,m1):
    running = True
    waiting = True
    cmd = ""
    while (running == True):
        cmd = input("Cmd: ")
        cmd = cmd.lower()

        if (cmd in ["map","check map"]):
            m1.check_map()
        elif (cmd in ["check demand", "demand", "dmd", "loc", "location"]):
            m1.curr_city.check_demand()
        elif (cmd in ["inv","inventory","stock","drugs"]):
            p1.check_inv()
        elif (cmd in ["go","travel","move"]):
            travel(p1,m1)
        elif (cmd == "sell"):
            plyr_sells(m1.curr_city.inventory, p1.inventory, drug_list)
        elif (cmd == "buy"):
            plyr_buys(m1.curr_city.inventory, p1.inventory, drug_list)
        # elif (cmd in ["auto buy","autobuy"]):
        #     auto_buy()
        # elif (cmd in ["auto sell","autosell"]):
        #     auto_sell()
        # utility
        elif (cmd == "help"):
            helper()
        elif (cmd == "exit" or cmd == "quit"):
            running = False
        elif (cmd == "clear"):
            for x in range(0, 300):
                print("\n")
        # unknown command
        else:
            print("Unknown Command!")
            print(" ")

def main():
    p1 = Player('jeff')
    m1 = Map(city_list[0], city_list)
    m1.curr_city.inventory.generate_qty(drug_list)

    print(Color.BOLD + Color.CYAN + "W E L C O M E  T O  C Y B E R - D O P E - W A R S  A L P H A" + Color.END)
    print(Color.BOLD + Color.YELLOW + "A Cyber-Punk Drug Dealing Sim By Mathieu Dombrock" + Color.END)
    helper()
    print(" ")
    print(" ")
    GameLoop(p1,m1)

    # p1 = Player('jeff')
    # m1 = Map(city_list[0], city_list)
    # m1.curr_city.inventory.generate_qty(drug_list)
    # m1.curr_city.check_demand()


if __name__ == '__main__':
    main()
