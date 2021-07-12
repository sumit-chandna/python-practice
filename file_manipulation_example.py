def write_file_demo():
    print("========")
    file = open("employees.txt", "w")
    lines = ["Jim - Salesman",
             "Dwight - Sales",
             "Pam - Receptionist",
             "Micheal - Manager",
             "Oscar - Accountant"]

    print(f"writing {lines} to file")
    for line in lines:
        file.write(line + "\n")
    file.close()
    print("========")


def append_file_demo():
    print("========")
    file = open("employees.txt", "a")
    lines = ["Ryan - Temp"]
    print(f"Appending {lines} to file")
    file.writelines(lines)
    file.close()
    print("========")


def read_file_demo():
    file = open("employees.txt", "r")
    print("\nReading \"employees.txt\" file")
    if file.readable():
        # print(file.read())
        # print(file.readline())
        for line in file.readlines():
            print(line)
    else:
        print("cannot read")
    file.close()
