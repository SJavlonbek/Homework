# from abc import ABC
import math

class Shape:

    def rectangle_surface(self):
        pass

    def perimeter_rectangle(self):
        pass

    def triangle_surface(self):
        pass

    def triangle_perimeter(self):
        pass

    def circle_suface(self):
        pass

    def circle_length(self):
        pass

class Rectangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def rectangle_surface(self):
        return f"Turtburchakni yuzi: {self.a * self.b} ga teng"

    def perimeter_rectangle(self):
        return f"Turtburchakni perimetri {2*(self.a + self.b)} ga teng"

class Triangle(Shape):
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def triangle_perimeter(self):
        return f"uchburchakni premitri {self.a + self.b + self.c} ga teng"

    def triangle_surface(self):
        return f"Uchburchakni yuzi {(((self.a + self.b + self.c)/2)*(((self.a + self.b + self.c)/2)-self.a)*(((self.a + self.b + self.c)/2)-self.b)*(((self.a + self.b + self.c)/2)-self.c))**(1/2)} ga teng"

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def circle_length(self):
        return f"Aylana uzunligi {2*math.pi*self.radius} ga teng"

    def circle_suface(self):
        return f"Aylana yuzi {math.pi*((self.radius)**2)} ga teng"


Rectangle1=Rectangle(7,8)
print(Rectangle1.rectangle_surface())
print(Rectangle1.perimeter_rectangle())

Triangle1=Triangle(3,4,5)
print(Triangle1.triangle_perimeter())
print(Triangle1.triangle_surface())

Circle1=Circle(5)
print(Circle1.circle_length())
print(Circle1.circle_suface())