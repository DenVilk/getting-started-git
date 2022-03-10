# class Contact:

# 	def __init__(self, name, email):
# 		self.name = name
# 		self.email = email

# class MailSenderMixin:

#     def send_mail(self, message):
#         print(f"Sending email to {self.email}")
#         print(f"{message}")


# class EmailableContact(Contact, MailSenderMixin):
#     pass

# cont = EmailableContact("Dmitriy", "dm@mail.ru")

# cont.send_mail("Hello world!")

# class E: pass
# class B(E): pass
# class C(E): pass
# class G(E): pass
# class F(E): pass
# class D(G, F): pass
# class A(B, C): pass
# class H(D, A): pass

# print(H.__mro__)
# print(E.__mro__)

from math import sqrt

class Rectangle:
    __width = 0
    __height = 0

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        # self.__area = self.__width * self.__height
    
    # @property
    def area(self):
        return self.__width * self.__height

    def resize(self, width, height):
        self.__height = height
        self.__width = width


class Square(Rectangle):

    def __init__(self, height):
        super().__init__(height, height)

    def resize(self, height):
        super().resize(height, height)
    

class Triangle:

    def __init__(self, side):
        self.__side = side

    @property
    def side(self):
        return self.__side

    # @property
    def area(self):
        return (self.__side ** 2) * (sqrt(3))/4


class RightPyramid(Triangle, Square):

    def __init__(self, side):
        Triangle.__init__(self, side)
        Square.__init__(self, side)

    # @property
    def area(self):
        return 4 * Triangle.area(self) + Square.area(self)


pyr = RightPyramid(4)
print(pyr.area())
print(RightPyramid.mro())