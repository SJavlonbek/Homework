class Person:
    def init(self,first_name,last_name,profession):
        self.first_name=first_name
        self.last_name=last_name
        self.profession=profession

    def person_info(self):
        return f"{self.first_name} {self.last_name}, kasbi {self.profession}"

class Teacher(Person):
    def init(self,first_name,last_name,profession,experience,speciality):
        super().init(first_name,last_name,profession)
        self.experience=experience
        self.speciality=speciality

    def action(self):
        return f"Siz  {self.speciality} yunalishida ishlar ekansiz"

    def update_experience(self,new_experience):
        old_experience=self.experience
        self.experience=new_experience
        return f"sizning oldingi ish tajribangiz {old_experience} yangisi {self.experience}"
    
    def Teacher_info(self):
        return f"{self.speciality} yunalishda {2023-self.experience} ishlar ekansiz"




person1=Teacher(input("Ismni kiriting:"),input("Familiya kiriting:"),input("Kasbni kiriting:"),int(input("tarjibani kiriting butun son:")),input("Yunalishni kiriting:"))
print(person1.person_info())
print(person1.action())
print(person1.update_experience(int(input("yangi tarjibani kiriting:"))))
print(person1.Teacher_info())