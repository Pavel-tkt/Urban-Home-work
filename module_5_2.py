class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors


    def go_to(self, new_floor):
        if 1 < new_floor < self.number_of_floors:
            for i in range(1, new_floor +1):
                print(i)
        else:
            print("Такого этажа не существует")


    def __len__(self):
        return self.number_of_floors



    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.number_of_floors}')

h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))