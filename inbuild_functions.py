from random import shuffle, randint


def inbuilt_functions_demo():
    my_list = [13, 3, 5, 6, 8, 1]
    print(f"my list : {my_list}")
    print(f"min value : {min(my_list)}")
    print(f"max value : {max(my_list)}")
    shuffle(my_list)
    print(f"shuffled list : {my_list}")
    print(f"random int : {randint(0, 100)}")
