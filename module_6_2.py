#необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.
#I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:


class Vehicle:


    __COLOR_VARIANTS = ['red', 'black', 'white', 'purple'] #Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)


    def __init__(self, owner, model, color, engine_power):
        self.owner = owner #Атрибут owner(str) - владелец транспорта. (владелец может меняться)
        self.__model = model  #Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = engine_power  #Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = color #Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)

#Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    # Каждый объект Vehicle должен содержать следующий методы:

    # Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    # Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    # Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'purple', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()
