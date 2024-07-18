import os

class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self. category = category


    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        if not os.path.isfile(self.__file_name):
            return ''
        file = open(self.__file_name, 'r')
        prod = file.read()
        file.close()
        return prod
    def add_prods(self, *products):
        prod = self.get_products()
        prod_2 = ''
        for i in products:
            if i.name in prod + prod_2:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                prod_2 += str(i) + '\n'
        if prod_2:
            file = open(self.__file_name, 'a')
            file.write(prod_2)
            file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add_prods(p1, p2, p3)

print(s1.get_products())
