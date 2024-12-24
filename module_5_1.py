
class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print("Такого этажа не существует")
        else:
            for i in range(1,new_floor + 1):
                print(i)


h1 = House("Бурдж-Халифа", 163)
h2 = House("Хрущевка", 5)
h1.go_to(170)
print("________________________________________")
h2.go_to(3)