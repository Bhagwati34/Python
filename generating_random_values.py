import random
for i in range(3):
    print(random.random())

for j in range(3):
    print(random.randint(0,20))

member = ["Bhagwati", "yash", "Abhinav", "Abhik"]
print(f"List of member: ")
for name in member:
    print(name)
leader = random.choice(member)
print(f"leader of team is : {leader}")

