from Chef import Chef
from ChineseChef import ChineseChef
from Student import Student


def class_demo():
    student1 = Student("Jim", "Business", 2.1, False)
    print(student1.name + " " + student1.on_honor_roll())
    student2 = Student("Phyllis", "Business", 3.8, False)
    print(f"{student2.name} {student2.on_honor_roll()}")

    chef = Chef("Skc")
    chef.make_special_dish()

    chef1 = ChineseChef("Skc")
    chef1.make_special_dish()
    chef1.make_salad()
