class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Drow")


point1 = Point(20, 30)
point1.x = 50  # update 'x' attribute
print(point1.x)
