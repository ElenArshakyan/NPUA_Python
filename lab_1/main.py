class Shape:
    def area(self):
        pass

    def volume(self):
        pass

class TwoDimensionalShape(Shape):
    pass

class ThreeDimensionalShape(Shape):
    pass

class Square(TwoDimensionalShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(TwoDimensionalShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Cube(ThreeDimensionalShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * (self.side ** 2)

    def volume(self):
        return self.side ** 3

class Cone(ThreeDimensionalShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        base_area = 3.14159 * (self.radius ** 2)
        side_area = 3.14159 * self.radius * ((self.radius ** 2) + (self.height ** 2)) ** 0.5
        return base_area + side_area

    def volume(self):
        return (1/3) * 3.14159 * (self.radius ** 2) * self.height

square = Square(side=4)
triangle = Triangle(base=4, height=5)

print("Area of Square:", square.area())
print("Area of Triangle:", triangle.area())

cube = Cube(side=3)
cone = Cone(radius=2, height=4)

print("Area of Cube:", cube.area())
print("Volume of Cube:", cube.volume())

print("Area of Cone:", cone.area())
print("Volume of Cone:", cone.volume())