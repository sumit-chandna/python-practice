def try_except_demo():
    try:
        # int_val = int(input("Enter a integer : "))
        # print(int_val)
        print(10 / 0)
    except ValueError as ve:
        print(f"Invalid input : {ve}")
    except ZeroDivisionError as zde:
        print(f"Divided by Zero : {zde}")
    except:
        print("Generic error")
