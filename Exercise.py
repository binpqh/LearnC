#numbers = [10, 15, 21, 30, 33, 42, 55]
#result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0 , numbers))
#print(result)
#numbers = [1, 4, 9, 16, 25]
#result = list(map(lambda x: x**0.5 , numbers))
#print(result)
from functools import reduce
numbers = [2, 3, 4, 5]
result = reduce(lambda x,y : x+y**2 , numbers)
print(result)