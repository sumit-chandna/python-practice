class Student:
    # Constructor
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return "on honor roll"
        else:
            return "not on honor roll"

    def __str__(self):
        return f"{self.name} : {self.major}"
