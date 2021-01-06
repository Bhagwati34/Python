class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, my name is {self.name}")
        print("English")


person1 = Person("Bhagwati")
#print(f"Name: {person1.name}")
person1.talk()

dangi = Person("Dangi")
dangi.talk()