from game import *
from inventory import *


class Map:
    def __init__(self, start_loc, locations):
        self.curr_city = City.from_list(start_loc)
        self.cities = [loc[0] for loc in locations]

    def check_map(self):
        print(" ")
        print(Color.RED + "M A P :" + Color.END)
        print(" ")
        print("Current Location: ", self.curr_city.name)
        print(" ")
        for city in self.cities:
            print(city.name)
        print(" ")
        print("----")
        print(" ")

    def travel(self, city):
        self.curr_city = City.from_list(find_item_info(city, city_list))

class City_inv(Inventory):
    '''The map's drug supply'''

    def __init__(self, city_name, type_keys):
        super().__init__(city_name)
        self.price_adj = random.uniform(.9, 1.5)
        self.qty_adj = random.uniform(.6, 2)
        self.type_keys = type_keys

    def generate_qty(self, drug_list):
        '''
        1. create a random number that will decide how many items to choose
        2. choose that number of items randomly from the game list
        3/4. choose random prices/qty for each (using the price/qty_adj
        5. add to the map inventory'''
        num_drugs = random.sample(drug_list, random.randint(1, len(drug_list)))
        for d in num_drugs:
            drug_supply = d[4] * random.randint(1, 10) / 6
            drug_demand = random.uniform(.3, 1.5)
            qty = round(self.qty_adj * drug_supply, 0)
            self.add_item(Item.from_list(d, qty))
            type_key = self.type_keys.get(d[1])
            self.items[d[0]].price = round(self.items[d[0]].price * self.price_adj * drug_demand * float(type_key), 2)
    
    def print_items(self):
        inv = [['Item:','Price:','Qty:','Type:','Info:']]
        for item in self.items.values():
            inv.append([str(x) for x in [item.name, item.price, item.qty, item.type, item.info]])
        colwidth = max(len(word) for row in inv for word in row[:-1]) + 2
        for row in inv:
            print("".join(word.ljust(colwidth) for word in row))


class City:
    def __init__(self, name, info, upper=1.0, downer=1.0, painkiller=1.0):
        self.name = name
        self.info = info
        type_keys = {'Upper': upper, 'Downer': downer, 'Painkiller': painkiller}
        self.inventory = City_inv(self.name, type_keys)

    @classmethod
    def from_list(cls, city_info):
        name, info, *c = city_info
        return cls(name, info, *c)

    def check_demand(self):
        print(Color.RED + "L O C A T I O N :" + Color.END)
        print("Current Location: ", self.name)
        print(" ")
        print("Location Information: ")
        print(self.info)
        print(" ")
        print(Color.RED + "D E M A N D :" + Color.END)
        print("Current Location: ", self.name)
        self.inventory.print_items()
        print(" ")


def travel(p1,m1):
    cost = round(random.uniform(0.1, 25.0), 2)
    destination = input("Where to?: ")
    city = destination.title()
    found = False
    if (p1.inventory.cash >= cost):
        for x in range(0, len(m1.cities)):
            if (destination in m1.cities):
                found = True
        if (found == False):
            print("I can't find this place.")
            print(" ")
        else:
            print("Found ", len(m1.cities), " on the map...")
            print("Traveling to ", destination, " for", cost, "$")
            print(" ")
            p1.inventory.cash = p1.inventory.cash - cost
            m1.travel(city)
            m1.curr_city.inventory.generate_qty(drug_list)
    else:
        print("you are too broke to travel! Try again later...")
        print(" ")



        
        
        












