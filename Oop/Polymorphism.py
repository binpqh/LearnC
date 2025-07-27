class Circle:
    def area(self):
        print("1")

class Square:
    def area(self):
        print("2")
none = [Circle(), Square()]
for a in none:
    a.area()