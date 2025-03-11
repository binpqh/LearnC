class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def greet(self):
        print("xin chao , toi la {self.name}, toi {self.age}tuoi.")
c1 = Student("Jack1cu5", 27)
c1.greet