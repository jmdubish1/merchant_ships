from game import *
from inventory import *


class Map:
    def __init__(self, start_loc, locations):
        self.curr_port = Port.from_list(start_loc)
        self.ports = [loc[0] for loc in locations]

    def show_map(self):
        print(" ")
        print(Color.red + "Ye' Ocean:" + Color.end)
        print(" ")
        print("Current Port: ", Color.cyan + self.curr_port.name + Color.end)
        print(" ")
        print(Color.underline + "Ports Nearby: " + Color.end)
        for port in self.ports:
            print(Color.green + port + Color.end)
        print(" ")

    def travel(self, port, port_list):
        self.curr_port = Port.from_list(find_item_info(port, port_list))


class Port:
    def __init__(self, name, info, spice=1.0, textile=1.0, 
                 alcohol=1.0, supplies=1.0, food=1.0, weapon=1.0):
        self.name = name
        self.info = info
        type_keys = {'Spice': spice,
                     'Textile': textile,
                     'Alcohol': alcohol,
                     'Supplies': supplies,
                     'Food': food,
                     'Weapon': weapon}
        self.inventory = Port_inv(self.name, type_keys)

    @classmethod
    def from_list(cls, port_info):
        name, info, *c = port_info
        return cls(name, info, *c)

    def check_demand(self):
        print(Color.red + "PORT OF CALL: " + Color.end)
        print("Current Port: ", self.name)
        print(" ")
        print("Port Information: ")
        print(self.info)
        print(" ")
        print(Color.red + "What's for sale, matey?:" + Color.end)
        print("Current Port: ", self.name)
        self.inventory.print_items()
        print(" ")


class Port_inv(Inventory):
    '''The map's item supply'''

    def __init__(self, port_name, type_keys):
        super().__init__(port_name)
        self.price_adj = random.uniform(.9, 1.5)
        self.qty_adj = random.uniform(.6, 2)
        self.type_keys = type_keys

    def generate_qty(self, item_list):
        '''
        1. create a random number that will decide how many items to choose
        2. choose that number of items randomly from the game list
        3/4. choose random prices/qty for each (using the price/qty_adj
        5. add to the map inventory'''
        num_items = random.sample(item_list, random.randint(1, len(item_list)-10))
        for d in num_items:
            item_supply = d[4] * random.uniform(.3, 1.5)
            item_demand = random.uniform(.3, 1.5)
            qty = round(self.qty_adj * item_supply, 0)
            self.add_item(Item.from_list(d, qty))
            type_key = self.type_keys.get(d[1])
            self.items[d[0]].price = round(self.items[d[0]].price * self.price_adj * item_demand * float(type_key), 2)
    
    def print_items(self):
        inv = [['Item:','Price:','Qty:','Type:','Info:']]
        for item in self.items.values():
            inv.append([str(x) for x in [item.name, item.price, item.qty, item.type, item.info]])
        colwidth = max(len(word) for row in inv for word in row[:-1]) + 2
        for row in inv:
            print("".join(word.ljust(colwidth) for word in row))


def travel(p1,m1, port_list, item_list):
    cost = round(random.uniform(0.1, 25.0), 2)
    destination = input("Heading, sir...: ")
    port = destination.title()
    found = False
    if (p1.inventory.cash >= cost):
        for x in range(0, len(m1.ports)):
            if (destination.title() in m1.ports):
                found = True
        if (found == False):
            print("We can't find this place.")
            print(" ")
        else:
            print("Found ", len(m1.ports), " on the map...")
            print("Setting Sail for ", destination, " for", cost, "pieces of gold")
            print(" ")
            p1.inventory.cash = p1.inventory.cash - cost
            m1.travel(port, port_list)
            loot_box(p1.inventory,item_list)
            m1.curr_port.inventory.generate_qty(item_list)
    else:
        print("you are too broke to sail! Sell something or risk mutiny!!!")
        print(" ")



        
        
        












