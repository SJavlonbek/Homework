class Car:
    def __init__(self,company_name,model,year,price,walking_path,strength):
        self.company_name=company_name
        self.model=model
        self._year=year
        self._price=price
        self.__walking_path=walking_path
        self.__strength=strength

    def get_info(self):
        return f"Bu mashina {self.company_name} zavodida ishlab chiqilgan va uning modeli {self.model} yili:{self._year} narxi:{self._price}$ bosib utgan yuli {self.get_private_walking()} km kuchi {self.get_private_strength()} ot kuchiga teng"

    def get_private_walking(self):
        return self.__walking_path
    
    def get_private_strength(self):
        return self.__strength

    def set_car_new(self,new_year,new_price,new_walking_path,new_strength):
        self._year=new_year
        self._price=new_price 
        self.__walking_path=new_walking_path
        self.__strength=new_strength                
        

    def get_info_new(self):
        return f"Mashina malumotlari uzgargandan sung Bu mashina {self.company_name} zavodida ishlab chiqilgan va uning modeli {self.model} yili:{self._year} narxi:{self._price}$ bosib utgan yuli {self.__walking_path} km kuchi {self.__strength} ot kuchiga teng"


car1=Car("Lamborghini","Lamborghini Aventador",2022,507353,2000,9000)
car2=Car("BMW","BMW XS",2022,200000,1500,4500)
car3=Car("Mercedes","Mercedes AMG G63",2022,500000,1000,10000)
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())
car1.set_car_new(2023,507000,8000,10000)
print(car1.get_info_new())
print(car2.get_info_new())
print(car3.get_info_new())

