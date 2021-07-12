class Chef:
    def __init__(self, name):
        self.name = name

    def make_chicken(self):
        print(f"The Chef \"{self.name}\" makes a chicken")

    def make_salad(self):
        print(f"The Chef \"{self.name}\" makes a salad")

    def make_special_dish(self):
        print(f"The Chef \"{self.name}\" makes bbq ribs")
