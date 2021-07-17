from Chef import Chef
from ChineseChef import ChineseChef
from Cylinder import Cylinder
from Line import Line
from Student import Student


def class_demo():
    student1 = Student("Jim", "Business", 2.1, False)
    print(student1)
    print(f"{student1.name}  {student1.on_honor_roll()}")
    student2 = Student("Phyllis", "Business", 3.8, False)
    print(student2)
    print(f"{student2.name} {student2.on_honor_roll()}")

    chef = Chef("Skc")
    chef.make_special_dish()

    chef1 = ChineseChef("Skc")
    chef1.make_special_dish()
    chef1.make_salad()
    print("========line class Example========")
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)
    line = Line(coordinate1, coordinate2)
    print(f"distance between {coordinate1}  and {coordinate2} : {line.distance()}")
    print(f"slope between {coordinate1}  and {coordinate2} : {line.slope()}")

    print("========cylinder class Example========")
    cylinder = Cylinder(2, 3)
    print(f"volume of {cylinder} : {cylinder.volume():1.2f}")
    print(f"surface area of {cylinder} : {cylinder.surface_area():1.1f}")
