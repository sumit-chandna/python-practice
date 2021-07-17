class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.radius * self.radius * self.height

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * self.height + 2 * Cylinder.pi * self.radius * self.radius

    def __str__(self):
        return f"Cylinder({self.height},{self.radius})"
