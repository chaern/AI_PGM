import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius
    
c1 = circle(5)
print(f"Circle with radius {c1.radius}:")
print(f"Area: {c1.area()}")
print(f"Circumference: {c1.circumference()}")
c2 = circle(10)
print(f"\nCircle with radius {c2.radius}:")
print(f"Area: {c2.area()}")
print(f"Circumference: {c2.circumference()}")

