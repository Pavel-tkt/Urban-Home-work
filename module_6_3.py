import random


#Animal - класс описывающий животных.
class Animal:
    live = True
    sound = None #звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #степень опасности существа

#Объект этого класса обладает следующими атрибутами:
#_cords = [0, 0, 0] - координаты в пространстве.
#speed = ... - скорость передвижения существа (определяется при создании объекта)
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

#И методами:
#move(self, dx, dy, dz), который должен менять соответствующие кооординаты в _cords на dx, dy и dz в том же порядке, где множетелем будет являтся speed.
    # Если при попытке изменения координаты z в _cords значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносятся.


    def move(self, dx, dy, dz):
        coord_x = self._cords[0] + int(dx) * int(self.speed)
        coord_y = self._cords[1] + int(dy) * int(self.speed)
        coord_z = self._cords[2] + int(dz) * int(self.speed)

        if coord_z < 0:
            print(f"It's too deep, i can't dive :(")
        else:
            self._cords =[coord_x, coord_y,coord_z]


    # get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")


# attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0" , если равно или больше.
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    # speak(self), который выводит строку со звуком sound.
    def spek(self):
        print(self.sound)


class Bird(Animal):
    beak = True #наличие клюва
    def lay_eggs(self):    #который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
        egg = random.randint(1, 4)
        print(f"Here are(is) {egg} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
#где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z в _coords.
# Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
# Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)
        coord_z = abs(self._cords[2]) - dz * self.speed // 2
        self._cords[2] = coord_z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


#Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
# Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"
    def speak(self):
        print(self.sound)

db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in(6)
db.get_cords()

db.lay_eggs()