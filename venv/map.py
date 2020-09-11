from game import *
from drugs import *

class Map:
    cities = []
    upper = 1.000
    downer = 1.000
    painkiller = 1.000
    one = 1.000
    two = 1.000

    def __init__(self, start_loc, city_list):
        self.location = start_loc
        for city in city_list:
            self.cities.append(city)

    def travel(self, city):
        self.location = city
        print(" ")
        print(Color.GREEN + "You Have arrived at ", self.location.name + Color.END)
        print(" ")
        # set new rates
        self.upper = round(random.uniform(0.1, 2.7), 3)
        self.downer = round(random.uniform(0.1, 2.7), 3)
        self.painkiller = round(random.uniform(0.1, 2.7), 3)
        self.one = round(random.uniform(0.7, 1.3), 3)
        self.two = round(random.uniform(0.8, 1.2), 3)

    def check_demand(self):
        print(" ")
        print(Color.RED + "D E M A N D :" + Color.END)
        print("Current Location: ", self.location.name)
        print(" ")
        print("Uppers: ", self.upper, "X")
        print("Downers: ", self.downer, "X")
        print("PainKillers: ", self.painkiller, "X")
        print(" ")
        print("Wheeze: ", round(float(Wheeze.price) * float(self.downer) * self.one, 4), "$")
        print("Stimpak: ", round(float(Stimpak.price) * float(self.painkiller) * self.one, 4), "$")
        print("Jet: ", round(float(Jet.price) * float(self.upper) * self.one, 4), "$")
        print("Kram: ", round(float(Kram.price) * float(self.upper) * self.two, 4), "$")
        print("Lsx: ", round(float(Lsx.price) * float(self.painkiller) * self.two, 4), "$")
        print("----")
        print(" ")

    def check_location(self):
        print(" ")
        print(Color.RED + "L O C A T I O N :" + Color.END)
        print("Current Location: ", self.location.name)
        print(" ")
        print("Location Information: ")
        print(self.location.info)
        print(" ")
        print("----")
        print(" ")

    def check_map(self):
        print(" ")
        print(Color.RED + "M A P :" + Color.END)
        print(" ")
        print("Current Location: ", self.location.name)
        print(" ")
        for city in self.cities:
            print(city.name)
        print(" ")
        print("----")
        print(" ")


class City:
    def __init__(self, name, info, upper=1.0, downer=1.0, painkiller=1.0):
        self.name = name
        self.info = info
        self.upper = float(upper)
        self.downer = float(downer)
        self.painkillter = float(painkiller)

city_list = [City("Victory","description",1.8,0.7),
             City("Arrival","description"),
             City("Boost","description",1.2,1.3,0.9)]


def travel(p1,m1):
    cost = round(random.uniform(0.1, 20.0), 3)
    destination = input("Where to?: ")
    destination = destination.title()
    found = False
    if (p1.cash >= cost):
        for x in range(0, len(m1.cities)):
            if (destination == m1.cities[x].name):
                print("Found ", m1.cities[x].name, " on the map...")
                found = True
                city = m1.cities[x]
        if (found == False):
            print("I can't find this place.")
            print(" ")
        else:
            print("Traveling to ", destination, " for", cost, "$")
            print(" ")
            p1.cash = p1.cash - cost
            m1.travel(city)
    else:
        print("you are too broke to travel! Try again later...")
        print(" ")
