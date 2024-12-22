
from pprint import pprint

#Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

#Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.

    def __str__(self):
        return f' {self.name}, {self.weight}, {self.category}'


class Shop:
    #Инкапсулированный атрибут __file_name = 'products.txt'.
    def __init__(self):
        self.__file_name = 'products.txt'

    #Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
    def get_products(self):
        self.file = open(self.__file_name, 'r')
        file_info =  self.file.read()
        self.file.close()
        return file_info



#Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products,
# если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
    def add(self, *products):
        add_new_product = self.get_products()
        for i in products:
            self.file = open(self.__file_name, 'a')
            if i.name not in add_new_product:
                self.file.write(f'{i}\n')
                self.file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())