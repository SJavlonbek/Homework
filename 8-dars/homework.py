class Car:
    def __init__(self, price, age):
        super().__init__()
        self.price = price
        self.age = age

class BMW:
    def __init__(self, model, strength):
        self.model = model
        self.strength = strength


class X7(BMW, Car):
    def __init__(self, price, age, model, strength):
        BMW.__init__(self, model, strength)
        Car.__init__(self, price, age)

    def X7_info(self):
        return f"mashni modeli {self.model} yili {self.age} narxi {self.price} kuchi {self.strength}"


car1 = X7(300000, 2022, "BMW X7", 5000)
print(car1.X7_info())
