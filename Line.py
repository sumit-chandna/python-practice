import math


class Line:
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        return math.sqrt(
            math.pow(self.coordinate2[0] - self.coordinate1[0], 2) + math.pow(self.coordinate2[1] - self.coordinate1[1],
                                                                              2))

    def slope(self):
        return (self.coordinate2[1] - self.coordinate1[1]) / (self.coordinate2[0] - self.coordinate1[0])
