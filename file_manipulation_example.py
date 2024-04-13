def write_file_demo():
    print("========")
    with open("employees.txt", mode="w") as file:
        lines = ["Jim - Salesman",
                 "Dwight - Sales",
                 "Pam - Receptionist",
                 "Micheal - Manager",
                 "Oscar - Accountant"]

        print(f"writing {lines} to file")
        for line in lines:
            file.write(line + "\n")
    print("========")


def append_file_demo():
    print("========")
    with open("employees.txt", mode="a") as file:
        lines = ["Ryan - Temp"]
        print(f"Appending {lines} to file")
        file.writelines(lines)
    print("========")


def read_file_demo():
    with open("employees.txt", mode="r") as file:
        print("\nReading \"employees.txt\" file")

        if file.readable():
            # print("file.seek(0) to move cursor to start of file")
            # file.seek(0)
            # print(file.read())
            # print(file.readline())
            for line in file.readlines():
                print(line)
        else:
            print("cannot read")
