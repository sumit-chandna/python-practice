from Chef import Chef


class ChineseChef(Chef):
    def __init__(self, name):
        super().__init__(name)

    def make_special_dish(self):
        print(f"The Chef \"{self.name}\" makes orange chicken")

    def make_fried_rice(self):
        print(f"The Chef \"{self.name}\" makes fired rice")
