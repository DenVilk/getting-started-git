# Inheritance
# Polymorphism
class Animal:
    name = ""

    def __init__(self, name):
        self.name = name

    def sound(self):
        print("...")

class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Gaf gaf")

dog = Dog(name = "Woofy")
animal = Animal(name = "Joe")

# print(dog.name)
# print(animal.name)

# dog.sound()
# animal.sound()

class Person:
    __id = 0
    name = ''
    surname = ''
    age = 0

    def __init__(self, name, surname, age, id):
        self.__id = id
        self.name = name
        self.surname = surname
        self.age = age

    def get_id(self):
        return self.__id


count = 0
man = Person('Vladimir','Velikovich', '123', count)
count += 1
print(man.get_id())
