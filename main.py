# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from app import *
from calculator import *
from class_example import *
from common_util import *
from condition_example import *
from dictonary_example import *
from file_manipulation_example import *
from function_example import *
from guess_one import *
from list_example import *
from loops_example import *
from palindrome import *
from rock_paper_scissors import *
from string_format_example import *
from try_except_example import *
from tuple_example import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_example()
    # input_example()
    print("========Calculator Example========")
    print(operation())
    # sum_of_numbers()
    # subtraction_of_numbers()
    # mad_libs()
    print("========List Example========")
    custom_list()
    print("========Tuple Example========")
    custom_tuple()
    print("========Function Example========")
    say_hi("kumar", 30)
    print(cube(3))
    print("========Condition Example========")
    if_else_gender(False, False)
    print(max_num(3, 5, 4))
    print("========Dictionary Example========")
    print(month_names("Dec"))
    print("========Loop Example========")
    while_demo()
    for_demo()
    print("========Try Except Example========")
    try_except_demo()
    print("========read file Example========")
    write_file_demo()
    read_file_demo()
    append_file_demo()
    read_file_demo()
    print("========Class Example========")
    class_demo()
    print("========String format Example========")
    string_format_demo()
    print("======== rock paper scissor Example========")
    play_game()
    print("========generate Password Example========")
    print(gen_password(8))
    print("========guessing Example========")
    guessing_game()
    print("========palindrome Example========")
    palindrome()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
