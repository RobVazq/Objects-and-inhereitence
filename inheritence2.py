class shape:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
class circle(shape):
    def __init__(self, X, Y, π):
        super().__init__(X, Y,)
        self.pi = 3.14

    def display1(self):
        return print((self.X * self.X)* self.pi, "Units Squared Circle")

class rectangle(shape):
    def __init__(self, X, Y):
        super().__init__(X, Y)

    def display2(self):
        return print((self.X * self.Y), "Units Squared Rectangle")

class Triangle(shape):
    def __init__(self, X, Y):
        super().__init__(X, Y)

    def display3(self):
        return print((self.X * self.Y) / 2, "Units Squared Triangle")

class Trapezoid(shape):
    def __init__(self, X, Y, Z):
        super().__init__(X, Y)
        self.Z = Z

    def display4(self):
        return print(((self.X + self.Z) * self.Y) / 2, "Units Squared Trapezoid/Trapezium")

# decided to have values that I have done myself
a = circle(2, 1, 3.14)
a.display1()
b = rectangle(20, 20)
b.display2()
c = Triangle(60, 20)
c.display3()
d = Trapezoid(15, 9, 7)
d.display4()

