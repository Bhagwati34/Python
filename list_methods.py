numbers = [2,3,4,6,8,7,8,10,7,78,56]
numbers.append(70)
print(numbers)
numbers.insert(0,40)
numbers.remove(7)
numbers.pop()
print(numbers.index(2))
print(10 in numbers)
print(numbers.count(8))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers)
numbers2 = numbers.copy()
numbers.append(89)
print(numbers2)
print(numbers)
numbers.clear()
