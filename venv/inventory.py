from game import *
from map import *
from drugs import *
import random



'''The drugs in the world'''
drug_list = [['Wheeze', 'Downer', 20, 'The chronic, the good shit. Classic', 50],
             ['Stimpak', 'Pain-Killer', 50, 'Keeps you going through the show', 40],
             ['Jet', 'Upper', 25, 'better than cocaine', 55],
             ['Kram', 'upper', 35, 'doinky doinky', 50],
             ['Lsx', 'Pain-Killer', 5, 'Bad drug man', 100],
             ['Prune-o', 'Downer', 3, 'Made in China', 90],
             ['The-Best', 'Upper', 95, 'No one really knows what it is', 10]]


class Item:
    '''Item details'''
    def __init__(self, name, type, price, info, qty):
        self.name = name
        self.type = type
        self.price = price
        self.info = info
        self.qty = qty

    @classmethod
    def from_list(cls, drug_info, qty):
        name, cat, price, info, _ = drug_info
        return cls(name, cat, price, info, qty)


class Inventory:
    '''Inventory super class'''
    def __init__(self, name):
        self.name = name
        self.cash = 0
        self.items = {}

    def add_item(self, _item):
        self.items[_item.name] = _item

    def print_items(self):
        inv = [['Item:','Price:','Qty:','Type:','Info:']]
        for item in self.items.values():
            inv.append([str(x) for x in [item.name, item.price, item.qty, item.type, item.info]])
        colwidth = max(len(word) for row in inv for word in row[:-1]) + 2
        for row in inv:
            print("".join(word.ljust(colwidth) for word in row))


class Plyr_inv(Inventory):
    '''The drugs you have'''
    def __init__(self, name):
        super().__init__(name)
        self.cash = 1000

class Map_inv(Inventory):
    '''The map's drug supply'''
    def __init__(self, map_name):
        super().__init__(map_name)
        self.price_adj = random.uniform(.9,1.1)
        self.qty_adj = random.uniform(.6,1.4)

    def generate_qty(self, drug_list):
        '''
        1. create a random number that will decide how many items to choose
        2. choose that number of items randomly from the game list
        3/4. choose random prices/qty for each (using the price/qty_adj
        5. add to the map inventory'''
        num_drugs = random.sample(drug_list,random.randint(1,len(drug_list)))
        for d in num_drugs:
            drug_demand = d[4]*random.randint(1,10)/6
            qty = round(self.qty_adj * drug_demand,0)
            self.add_item(Item.from_list(d, qty))
            self.items[d[0]].price = round(self.items[d[0]].price * self.price_adj, 2)