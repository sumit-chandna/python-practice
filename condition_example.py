def if_else_gender(is_male, is_tall):
    if is_male and is_tall:
        print("You are a tall male")
    elif is_male or is_tall:
        print("You are tall or male")
    else:
        print("Neither Male nor tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num3:
        return num2
    else:
        return num3
