def main():
    print("lalala")
    circle = Circle(5)
    print(f"circle.radius is: {circle.radius}")
    print(f"circle.area is: {circle.area}")
    circle.radius = 8
    print(f"circle.radius is: {circle.radius}")
    print(f"circle.area is: {circle.area}")



class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('radius must not be negative')
        self._radius = radius

    @property
    def area(self):
        return 2 * self.radius * self.radius * 3.14
    
main()
