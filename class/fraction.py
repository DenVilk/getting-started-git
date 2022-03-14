
from math import gcd


def wrapper(func):

    def a(a, b):
        # print(a, b)
        if isinstance(b, Drob):
            return func(a, b)
        else:
            raise TypeError
    
    return a

class Drob:
    num = 0
    denum = 1

    def __init__(self, c, z):
        self.num = c
        if z==0:
            print('Znamentel ne mozhet bit\' raven 0, stavim 1')
            self.denum = 1
        else: self.denum = z

    def __str__(self):
        return f'{self.num}/{self.denum}'

    def __repr__(self):
        return f'<Drob {self.num}/{self.denum}>'

    @wrapper
    def __add__(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        nod = gcd(abs(num), abs(denum))
        return Drob(num//nod, denum//nod)
    
    @wrapper
    def __sub__(self, other):
        num = self.num * other.denum - other.num * self.denum
        denum = self.denum * other.denum
        nod = gcd(abs(num), abs(denum))
        return Drob(num//nod, denum//nod)

    @wrapper
    def __mul__(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum
        nod = gcd(abs(num), abs(denum))
        return Drob(num//nod, denum//nod)

    @wrapper
    def __truediv__(self, other):
        num = self.num * other.denum
        denum = self.denum * other.num
        nod = gcd(abs(num), abs(denum))
        return Drob(num//nod, denum//nod)
        
    @wrapper
    def __lt__(self, other):
        res = eval(f'{self.num}/{self.denum} - {other.num}/{other.denum}')
        return res < 0
        

s1 = Drob(1,0)
s2 = Drob(2,3)
print(s1)
print(s2)
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
print(s2<s1)