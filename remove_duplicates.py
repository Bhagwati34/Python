number = [2, 3, 56, 78, 3, 6, 89, 56]
num2 = []
for num in number:
    if num not in num2:
        num2.append(num)
print(num2)