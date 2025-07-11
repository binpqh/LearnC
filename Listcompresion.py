numbers = range(1,31)
result = [num **2 for num in numbers if num % 3 == 0 and num % 2 != 0]
print(result)

