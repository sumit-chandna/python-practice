def sum_of_numbers():
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter another number:"))
    result = num1 + num2
    print(result)


def subtraction_of_numbers():
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter another number:"))
    result = num1 - num2
    print(result)


def operation():
    num1 = float(input("Enter a number:"))
    op = input("Enter the Operator:")
    num2 = float(input("Enter another number:"))
    if op == "+":
        sum_op = num1 + num2
        return f"{num1} + {num2} = {sum_op}"
    elif op == "-":
        minus = num1 - num2
        return f"{num1} - {num2} = {minus}"
    elif op == "*":
        multi = num1 * num2
        return f"{num1} * {num2} = {multi}"
    elif op == "/":
        divide = num1 / num2
        return f"{num1} / {num2} = {divide}"
    else:
        print("Invalid Operator")

    result = num1 - num2
    print(result)
