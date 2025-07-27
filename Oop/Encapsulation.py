class Person:
    def init(self,age):
        self.__age = age

    def set_age(self, age):
        self.__age >= 0
    
    def get_age(self):
        return self.__age