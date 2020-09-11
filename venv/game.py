import random
import numpy as np
from map import *
from drugs import *

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

class Player:
    def __init__(self, name):
        self.name = name

    cash = 1500
    _Wheeze = 30
    _Stimpak = 0
    _Jet = 0
    _Kram = 0
    _Lsx = 0

    def check_inv(self):
        print(" ")
        print(Color.RED + "I N V E N T O R Y :" + Color.END)
        print(" ")
        print("Cash:    ", self.cash)
        print(" ")
        print("Wheeze:  ", self._Wheeze)
        print("Stimpak: ", self._Stimpak)
        print("Jet:     ", self._Jet)
        print("Kram:    ", self._Kram)
        print("Lsx:     ", self._Lsx)
        print(" ")
        print("----")
        print(" ")


def sell():
    found = False
    item = input("Sell what?: ")
    item = item.title()
    amt = input("Ok, how much do you want to sell?: ")
    if (amt.isdigit() == True):
        print("Selling", amt, "", item, ".")
        print(" ")
    else:
        print("Please enter an integer for the amount.")
        print(" ")
    


    if (item == "Wheeze"):
        found = True
        if (p1._Wheeze >= int(amt)):
            price = (float(Wheeze.price) * m1.downer * m1.one) * float(amt)
            p1._Wheeze = p1._Wheeze - int(amt)
            p1.cash = p1.cash + (price)
            print("Sold", item, "for", price)
            print(" ")
        else:
            print("You don't have enough of that!")
            print(" ")

    elif (item == "Jet"):
        found = True
        if (p1._Jet >= int(amt)):
            price = (float(Jet.price) * m1.upper * m1.one) * float(amt)
            p1._Jet = p1._Jet - int(amt)
            p1.cash = p1.cash + (price)
            print("Sold", item, "for", price)
        else:
            print("You don't have enough of that!")
            print(" ")

    elif (item == "Stimpak"):
        found = True
        if (p1._Stimpak >= int(amt)):
            price = (float(Stimpak.price) * m1.painkiller * m1.one) * float(amt)
            p1._Stimpak = p1._Stimpak - int(amt)
            p1.cash = p1.cash + (price)
            print("Sold", item, "for", price)
        else:
            print("You don't have enough of that!")
            print(" ")

    elif (item == "Kram"):
        found = True
        if (p1._Kram >= int(amt)):
            price = (float(Kram.price) * m1.upper * m1.two) * float(amt)
            p1._Kram = p1._Kram - int(amt)
            p1.cash = p1.cash + (price)
            print("Sold", item, "for", price)
        else:
            print("You don't have enough cash to buy that!")
            print(" ")

    elif (item == "Lsx"):
        found = True
        if (p1._Lsx >= int(amt)):
            price = (float(Lsx.price) * m1.painkiller *m1.two) * float(amt)
            p1._Lsx = p1._Lsx - int(amt)
            p1.cash = p1.cash + (price)
            print("Sold", item, "for", price)
        else:
            print("You don't have enough cash to buy that!")
            print(" ")

    else:
        print("I can't find this item.")

def buy():
    found = False
    item = input("Buy what?: ")
    item = item.title()
    amt = input("Ok, how much do you want to buy?: ")
    if (amt.isdigit() == True):
        print("Buying", float(amt), "", item, ".")
        print(" ")
    else:
        print("Please enter an integer for the amount.")
        print(" ")

    if (item == "Wheeze"):
        found = True
        price = (float(Wheeze.price) * m1.downer * m1.one) * float(amt)
        if (p1.cash >= price):
            p1._Wheeze = p1._Wheeze + int(amt)
            p1.cash = p1.cash - (price)
            print("Bought", item, "for", price)
            print(" ")
        else:
            print("You don't have enough cash to buy that!")
            print(" ")

    elif (item == "Jet"):
        found = True
        price = (float(Jet.price) * m1.upper * m1.one) * float(amt)
        if (p1.cash >= price):
            p1._Jet = p1._Jet + int(amt)
            p1.cash = p1.cash - (price)
            print("Bought", item, "for", price)
        else:
            print("You don't have enough cash to buy that!")
            print(" ")

    elif (item == "Stimpak"):
        found = True
        price = (float(Stimpak.price) * m1.painkiller * m1.one) * float(amt)
        if (p1.cash >= price):
            p1._Stimpak = p1._Stimpak + int(amt)
            p1.cash = p1.cash - (price)
            print("Bought", item, "for", price)
        else:
            print("You don't have enough cash to buy that!")
            print(" ")

    elif (item == "Kram"):
        found = True
        price = (float(Kram.price) * m1.upper * m1.two) * float(amt)
        if (p1.cash >= price):
            p1._Kram = p1._Kram + int(amt)
            p1.cash = p1.cash - (price)
            print("Bought", item, "for", price)
        else:
            print("You don't have enough cash to buy that!")
            print(" ")

    elif (item == "Lsx"):
        found = True
        price = (float(Lsx.price) * m1.painkiller * m1.two) * float(amt)
        if (p1.cash >= price):
            p1._Lsx = p1._Lsx + int(amt)
            p1.cash = p1.cash - (price)
            print("Bought", item, "for", price)
        else:
            print("You don't have enough cash to buy that!")
            print(" ")

    else:
        print("I can't find this item.")

def auto_buy():
    prices = [(float(Wheeze.price) * m1.downer * m1.one),
              (float(Jet.price) * m1.upper * m1.one),
              (float(Stimpak.price) * m1.painkiller * m1.one),
              (float(Kram.price) * m1.upper * m1.two),
              (float(Lsx.price) * m1.painkiller * m1.two)]
    drug_list = ['Wheeze','Jet','Stimpak','Kram','Lsx']
    avg_prices = list(np.true_divide(prices,[20,50,25,35,5]))
    best_ind = avg_prices.index(min(avg_prices))
    item = drug_list[best_ind]
    best_price = prices[best_ind]
    ###Leave $40 for bus fare###
    amt = int((p1.cash - 40) / best_price)
    price = round(float(best_price) * amt,2)
    p1.cash = p1.cash - (price)
    if (item == "Wheeze"):
        p1._Wheeze += amt
        print("Bought", item, "for", price)
        print(" ")
    elif (item == "Jet"):
        p1._Jet += amt
        print("Bought", item, "for", price)
        print(" ")
    elif (item == "Stimpak"):
        p1._Stimpak += amt
        print("Bought", item, "for", price)
        print(" ")
    elif (item == "Kram"):
        p1._Kram += amt
        print("Bought", item, "for", price)
        print(" ")
    elif (item == "Lsx"):
        p1._Lsx += amt
        print("Bought", item, "for", price)
        print(" ")
    else:
        print("Not enough money to autobuy!")

def auto_sell():
    sell_p = input("What margin?: ")
    sell_p = sell_p.title()
    drug_list = []
    if p1._Wheeze > 0:
        drug_list.append('Wheeze')
    if p1._Stimpak > 0:
        drug_list.append('Stimpak')
    if p1._Jet > 0:
        drug_list.append('Jet')
    if p1._Kram > 0:
        drug_list.append('Kram')
    if p1._Lsx > 0:
        drug_list.append('Lsx')

    for item in drug_list:
        if (item == "Wheeze"):
            price = (float(Wheeze.price) * m1.downer * m1.one) * p1._Wheeze
            if price >= float(sell_p)*20:
                p1.cash = p1.cash + (price)
                p1._Wheeze -= p1._Wheeze
                print("Sold", item, "for", price)
                print(" ")
            else:
                print("Prices not good enough to sell!!")
        elif (item == "Jet"):
            price = (float(Jet.price) * m1.upper * m1.one) * p1._Jet
            if price >= float(sell_p)*50:
                p1.cash = p1.cash + (price)
                p1._Jet -= p1._Jet
                print("Sold", item, "for", price)
                print(" ")
            else:
                print("Prices not good enough to sell!!")
        elif (item == "Stimpak"):
            price = (float(Stimpak.price) * m1.painkiller * m1.one) * p1._Stimpak
            if price >= float(sell_p)*25:
                p1.cash = p1.cash + (price)
                p1._Stimpak += p1._Stimpak
                print("Sold", item, "for", price)
                print(" ")
            else:
                print("Prices not good enough to sell!!")
        elif (item == "Kram"):
            price = (float(Kram.price) * m1.upper * m1.two) * p1._Kram
            if price >= float(sell_p)*35:
                p1.cash = p1.cash + (price)
                p1._Kram -= p1._Kram
                print("Sold", item, "for", price)
                print(" ")
            else:
                print("Prices not good enough to sell!!")
        elif (item == "Lsx"):
            price = (float(Lsx.price) * m1.painkiller * m1.two) * p1._Lsx
            if price >= float(sell_p)*5:
                p1.cash = p1.cash + (price)
                p1._Lsx -= p1._Lsx
                print("Sold", item, "for", price)
                print(" ")
            else:
                print("Prices not good enough to sell!!")
    print("Done Selling")

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
        elif (cmd in ["loc","location"]):
            m1.check_location()
        elif (cmd in ["inv","inventory","stock","drugs"]):
            p1.check_inv()
        elif (cmd in ["go","travel","move"]):
            travel(p1,m1)
        elif (cmd in ["demand", "dmd"]):
            m1.check_demand()
        elif (cmd == "sell"):
            sell()
        elif (cmd == "buy"):
            buy()
        elif (cmd in ["auto buy","autobuy"]):
            auto_buy()
        elif (cmd in ["auto sell","autosell"]):
            auto_sell()
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

    print(Color.BOLD + Color.CYAN + "W E L C O M E  T O  C Y B E R - D O P E - W A R S  A L P H A" + Color.END)
    print(Color.BOLD + Color.YELLOW + "A Cyber-Punk Drug Dealing Sim By Mathieu Dombrock" + Color.END)
    helper()
    print(" ")
    print(" ")
    GameLoop(p1,m1)
if __name__ == '__main__':
    main()
