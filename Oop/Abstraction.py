#from abc import ABC, abstractmethod
#class Shape:
  # @abstractmethod
   # def area(self):
  #      pass

#class Triangle(Shape):
    #def area(self):
       # print("10")
        #Exercises
#from abc import ABC, abstractmethod
#class Animal(ABC):
  #  def __init__(self, name):
       # self.name = name
     #   self.__age = 0
  #  @abstractmethod
   # def make_sound(self):
   #     pass

   # def set_age(self, age):
       # if age >= 0:
            #self.__age = age
  #  def get_age(self):
     #   return self.__age


#class Dog(Animal):
   # def make_sound(self):
       # print("woof")

#class Cat(Animal):
    #def make_sound(self):
    #    print("meoo")

#class Parrot(Animal):
    #def make_sound(self):
     #   print("Squawk")

#dog = Dog("concho")
#cat = Cat("conmeo")
#parrot = Parrot("convet")

#dog.set_age(3)
#cat.set_age(2)
#parrot.set_age(1)

#none = [dog, cat, parrot]
#for a in none:
  ## a.make_sound()



from abc import ABC, abstractmethod
class Emloyee(ABC):
    def __init__(self, name , salary):
        self.name = name
        self.__salary = salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
    def get_salary(self):
        return self.__salary
    def get_total_income(self):
        return self.get_salary() + self.calculate_bonus()
    @abstractmethod
    def calculate_bonus(self):
        pass

class Manager(Emloyee):
    def calculate_bonus(self):
        return self.get_salary() * 0.5

class Staff(Emloyee):
    def calculate_bonus(self):
        return self.get_salary() * 0.2

manager = Manager("Huy", 500)
staff = Staff("Hyy", 200)

none = [manager, staff]
for a in none:
    print(f"Name: {a.name}, Salary: {a.get_salary()} , Bonus: {a.calculate_bonus()}, Total income : {a.get_total_income()}")
    a.calculate_bonus()


