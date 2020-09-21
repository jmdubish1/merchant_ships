from game import *
from map import *
import random

class Item:
    '''Item details'''
    def __init__(self, name, type, price, info, qty):
        self.name = name
        self.type = type
        self.price = price
        self.info = info
        self.qty = qty

    @classmethod
    def from_list(cls, item_info, qty):
        name, cat, price, info, _ = item_info
        return cls(name, cat, price, info, qty)

class Inventory:
    '''Inventory super class'''
    def __init__(self, name):
        self.name = name
        self.cash = 0
        self.items = {}

    def add_item(self, _item):
        self.items[_item.name] = _item


class Plyr_inv(Inventory):
    '''The items you have'''
    def __init__(self, name):
        super().__init__(name)
        self.cash = 500
    
    def print_items(self):
        inv = [['Item:','Qty:','Type:','Info:']]
        for item in self.items.values():
            if item.qty > 0:
                inv.append([str(x) for x in [item.name, item.qty, item.type, item.info]])
        colwidth = max(len(word) for row in inv for word in row[:-1]) + 2
        for row in inv:
            print("".join(word.ljust(colwidth) for word in row))

  

def plyr_buys(port_inv, plyr_inv, item_list):
    item = input("What are you trying to buy?: ")
    item = item.title()
    qty = input("How many do you want to buy?: ")
    if qty.isdigit():
        print("Making Buy: %s of %s..." % (qty, item))
        print(" ")
        '''Buying for player, changing both inventories. Accounting for whether both are able to make trade (Cash, Inv)'''
        too_many, enough_cash = False, False
        qty = float(qty)
        if item in port_inv.items:
            if qty > port_inv.items[item].qty:
                qty = port_inv.items[item].qty
                too_many = True
    
            if plyr_inv.cash >= qty * port_inv.items[item].price:
                enough_cash = True
                plyr_inv.add_item(Item.from_list(find_item_info(item, item_list), qty))
                plyr_inv.cash -= qty * port_inv.items[item].price
                port_inv.items[item].qty -= qty
                message_f = "You bought %s %s at %s each. Total: %s pieces of gold" % (item, qty, 
                                                                                       port_inv.items[item].price,
                                                                                       port_inv.items[item].price * qty)
                print(" ")
    
            if enough_cash == False:
                print("You don\'t have enough money")
                print(" ")
            elif too_many == True and enough_cash == True:
                print("You asked for more than the supplier could get. \n", message_f)
                print(" ")
            else:
                print(message_f)
                print(" ")

        else:
            print("Item not available")
            print(" ")
    else:
        print("Please enter an integer for amount")
        print(" ")



def plyr_sells(port_inv, plyr_inv, item_list):
    item = input("What are you trying to sell?: ")
    item = item.title()
    qty = input("How many do you want to sell?: ")
    if qty.isdigit():
        print("Making Sale: %s of %s..." % (qty, item))
        print(" ")

        '''Selling for player, changing both inventories. 
        Accounting for whether both are able to make trade (Cash, Inv)'''
        too_many = False
        qty = float(qty)
        if item in plyr_inv.items:
            if qty > plyr_inv.items[item].qty:
                qty = plyr_inv.items[item].qty
                too_many = True
            if item in port_inv.items:
                plyr_inv.cash += qty * port_inv.items[item].price
                plyr_inv.items[item].qty -= qty
                message_f = "You sold %s %s at %s each. \n Total: %s pieces of gold" % \
                            (item, qty, port_inv.items[item].price, port_inv.items[item].price * qty)
                port_inv.items[item].qty += qty
            else:
                price = find_item_info(item, item_list)
                plyr_inv.cash += qty * price[2]
                plyr_inv.items[item].qty -= qty
                message_f = "You sold %s %s at %s each. \n Total: %s pieces of gold" % \
                            (item, qty, price[2], price[2] * qty)
                port_inv.add_item(Item.from_list(find_item_info(item, item_list), qty))

            print(" ")

            if too_many == True:
                print("You tried to sell more than you have. \n", message_f)
                print(" ")
            else:
                print(message_f)
                print(" ")
    
        else:
            print("You don't own this item")
            print(" ")
    else:
        print("Please enter an integer for amount")
        print(" ")

        
def find_item_info(item, list):
    for r in range(0,len(list)):
        if item.title() in list[r][0]:
            return list[r]

def loot_box(plyr_inv, item_list):
    if random.uniform(0,1) < .05:
        plyr_inv.add_item(Item.from_list(find_item_info('Treasure Chest', item_list), 1.0))
        print('\033[1m' + '\033[91m' + "You found the X! Check your inventory!" + '\033[0m')
