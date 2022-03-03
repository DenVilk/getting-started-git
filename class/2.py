# class Soda:

#     def __init__(self, ingridient=None):
#         if isinstance(ingridient, str):
#             self.ingridient = ingridient
#         else:
#             self.ingridient = None

#     def show_my_drink(self):
#         if self.ingridient:
#             print(f'Газировка с {self.ingridient}')
#         else:
#             print(f'Обычная газировка')


# drink1 = Soda('малина')
# drink2 = Soda()
# drink3 = Soda(3)

# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()

# class Rectangle:
#     '''
#         Класс прямоугольника
#         Имеет длину и ширину
#     '''
#     __width = 0
#     __height = 0

#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height

#     def get_width(self):
#         '''
#             Функция получения ширины
#             данного прямоугольника
#         '''
#         return self.__width

#     def get_height(self):
#         '''
#             Функция получения высоты
#             данного прямоугольника
#         '''
#         return self.__height

#     def get_area(self):
#         '''
#             Функция получения площади
#             данного прямоугольника
#         '''
#         return self.__width * self.__height

# r1 = Rectangle(10, 5)
# r2 = Rectangle(2.5, 3)

# print(r1.get_area())
# print(r2.get_area())

# print(r1.get_height())
# print(r2.get_width())

# class KgToPounds:

#     __kg = 0

#     def __str__(self):
#         return f'{self.__kg}kg это {self.pounds}pounds'

#     def __init__(self, kg):
#         self.__kg = kg

#     @property
#     def kg(self):
#         return self.__kg

#     @kg.setter
#     def kg(self, kg):
#         self.__kg = kg

#     @property
#     def pounds(self):
#         return self.__kg * 2.205

# k = KgToPounds(15)

# print(k)

# print(k.pounds)
# print(k.kg)
# # k.set_kg(20)
# k.kg = 20
# print(k.pounds)
# print(k.kg)


class Book:
    name = ''
    author = ''
    pages = 0
    year = 0
    shops = []

    def __init__(self, name, author, pages, year, shops):
        self.name = name
        self.author = author
        self.pages = pages
        self.year = year
        self.shops = shops

    def __str__(self):
        return f'Книга {self.name} автора {self.author}'

    def __repr__(self):
        return f'Книга {self.name} автора {self.author}'

    def __eq__(self, other):
        if isinstance(other, Book):
            return len(self.shops) == len(other.shops)
    
    def __lt__(self, other):
        if isinstance(other, Book):
            return len(self.shops) < len(other.shops)

    def __gt__(self, other):
        if isinstance(other, Book):
            return len(self.shops) > len(other.shops)


b1 = Book(
    'Маленький принц', 
    "Антуан де Сент Экзюпери",
    200, 
    1954, 
    ['OZ', 'BELKNIGA']
)

b2 = Book(
    'Азбука',
    "Антуан де Сент Экзюпери",
    20,
    2003,
    ['OZ']
)

b3 = Book(
    'Не Азбука',
    "Антуан де Сент Экзюпери",
    150,
    2011,
    ['OZ', 'Belkniga', 'Buslik','Evroopt']
)


a = [b1,b2,b3]
a.sort()
print(a)

if b1 == 'abcd':
    print('EQ')
if b1 > b2:
    print('GT')
if b1 < b2:
    print('GT')