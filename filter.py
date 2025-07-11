numbers = [2, 4, 5, 7, 8, 10, 13]
result = list(filter(lambda x: x % 2 == 0 and x > 5 , numbers))
print(result)