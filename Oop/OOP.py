#class Car:
    
#    def __init__(self,brand,model,years):
#        self.brand = brand
#        self.model = model
#        self.years = years
    
#    def Display_info(self):
#        print(f" Brand :{self.brand} , Model : {self.model} , Years : {self.years} ")
#    def is_old(self):
#       return self.years < 2010

#brand = str(input("Please enter brand :"))

#model = str(input("Please enter model :"))

#years = int(input("please enter years :"))

#my_car = Car(brand, model, years)

#my_car.Display_info()

#f my_car.is_old():
#    print("this car is old.")
#else:
#   print("this car is new.")


class Product:
    
    def __init__(self, name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def Display_info(self):
        print(f"Name : {self.name} , Price : {self.price} , Quantity : {self.quantity}")
    
    def total_value(self):
        return self.price * self.quantity

name = str(input("Please enter name :"))

price = float(input("Please enter price :"))

quantity = int(input("Please enter quantity :"))

my_product = Product(name , price , quantity)

my_product.Display_info()

my_product.total_value()
print("Total value in stocks :" , my_product.total_value())

