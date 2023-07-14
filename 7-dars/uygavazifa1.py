class Car:
    def __init__(self,brand,max_speed,price):
        self.__brand=brand
        self.__max_speed=max_speed
        self.__price=price

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self,brand):
        self.__brand=brand
    @brand.deleter
    def brand(self):
        del self.__brand
    @property
    def max_speed(self):
        return self.__max_speed
    @max_speed.setter
    def max_speed(self,max_speed):
        self.__max_speed=max_speed
    @max_speed.deleter
    def max_speed(self):
        del self.__max_speed
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price=price
    @price.deleter
    def price(self):
        del self.__price
car1=Car("BMW",300,200000)
car2=Car("Lomborghini",400,500000)
car3=Car("Audi",320,250000)
print(car1.brand)
car2.max_speed=450
print(car2.max_speed)
car3.price=170000
print(car3.price)