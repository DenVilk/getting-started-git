import math

class Rectangle:
    __width = 0
    __height = 0

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__area = self.__width * self.__height
    
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, h):
        self.resize(h[0], h[1])
        self.__area = self.__width * self.__height

    def resize(self, width, height):
        self.__height = height
        self.__width = width


class Square(Rectangle):

    def __init__(self, height):
        super().__init__(height, height)

    def resize(self, height):
        super().resize(height, height)

class Romb(Square):
    __angle = 0

    def __init__(self, side, angle):
        super().__init__(side)
        self.__angle = angle

    @property
    def area(self):
        return super().area * math.sin(self.__angle*math.pi/180)

r1 = Rectangle(3, 5)
print(r1.area)
r1.resize(2, 5)
print(r1.area)

# r2 = Square(3)
# print(r2.area)
# r2.resize(2)
# print(r2.area)

# class Person:

#     def __init__(self, name, job=None, base_pay=0, part_time=1):
#         self.__name = name
#         self.__job = job
#         self.__base_pay = base_pay
#         self.__part_time = part_time

#     @property
#     def pay(self):
#         return self.__part_time * self.__base_pay

#     def __str__(self):
#         return f'[Person \'{self.__name}\' pay:{self.pay}, job:{self.__job}]'


# class Teacher(Person):

#     def __init__(self, name, base_pay=0, part_time=1, hours=0):
#         super().__init__(name, 'teacher', base_pay, part_time)
#         self.__hours = hours

#     @property
#     def pay(self):
#         return super().pay + self.__hours * 20


# class Programmer(Person):

#     def __init__(self, name, base_pay=0, part_time=1, languages=[]):
#         super().__init__(name, 'programmer', base_pay, part_time)
#         self.__languages = languages

#     def add_language(self, language):
#         self.__languages.append(language)

#     def check_language(self, language):
#         return language in self.__languages
#         # if language in self.__languages:
#         #     return True
#         # return False

    


# p1 = Person("Vladimir", 'Mentor', 600, 1.5)

# print(p1)
# print(p1.pay)

# p2 = Teacher('Vadim', 500, 1, 20)

# print(p2)

# p3 = Programmer('Artem', 5, 2, ['C++','Python','Pascal'])
# print(p3)
# print(p3.check_language('C#'))
# p3.add_language("C#")
# print(p3.check_language('C#'))

class UpgradedList(list):

    def max3(self):
        for i in self:
            if not isinstance(i, int):
                return None

        a = self.copy()
        a.sort(reverse=True)
        b = []
        for i in range(3):
            b.append(a[i])
        return tuple(b)

    def max_length(self):
        mx = 0
        x = 0
        for i in self:
            if len(str(i))>mx:
                mx = len(str(i))
                x = i
        return x, mx


a = UpgradedList([2,5,1123123,3,8,0,'str'])
print(a.max3())
print(a.max_length())