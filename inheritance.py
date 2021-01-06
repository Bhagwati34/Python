class Main:
    def walk(self):
        print("walk")


class Dog(Main):
    def bark(self):
        print("Bark")


class Cat(Main):
    def eat(self):
        print("Eat")


dog1 = Dog()
dog1.bark()
dog1.walk()


cat1 = Cat()
cat1.eat()
cat1.walk()

