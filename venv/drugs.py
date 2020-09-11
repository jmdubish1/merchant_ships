from game import *
from map import *
from drugs import *

class Item:
    def __init__(self, name, cat, price, info):
        self.name = name
        self.cat = cat
        self.price = price
        self.info = info
    
    @classmethod
    def from_list(cls, drug_info):
        name, cat, price, info = drug_info
        return cls(name, cat, price, info)

drug_list = [Item('Wheeze', 'Downer', '20','The chronic, the good shit. Classic'),
             Item('Stimpak', 'Pain-Killer', '50', 'Keeps you going through the show'),
             Item('Jet', 'Upper', '25', 'better than cocaine'),
             Item('Kram','upper','35', 'doinky doinky'),
             Item('Lsx','Pain-Killer','5','Bad drug man'),
             Item('Prune-o','Downer','3','Made in China')]