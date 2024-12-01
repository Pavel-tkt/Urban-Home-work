class House:
    # В классе House создаем атрибут houses_history = [], который будет хранить названия созданных объектов.
    houses_history = []

    # Дополняем метод __new__ так, чтобы:
    # 1. Название объекта добавлялось в список cls.houses_history.
    # 2. Название строения можно взять из args по индексу.
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

#Также переопределите метод __del__(self) в котором будет выводиться строка: "<название> снесён, но он останется в истории"
    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')


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



    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self,other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)