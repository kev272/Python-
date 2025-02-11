class Shape:
    def draw(self):
        print("Drawing a Shape")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

class square(Shape):
    def draw(self):
        print("Drawing a square")

sh = Shape()
sh.draw()

r = Rectangle()
r.draw()

s = square()
s.draw()
