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
from madlibs import *
from palindrome import *
from rock_paper_scissors import *
from string_format_example import *
from tic_tac_toe_game import *
from try_except_example import *
from tuple_example import *
from enumerate import *
from inbuild_functions import *
from set_example import *

if __name__ == '__main__':
    print("all example                      : 0")
    print("print format example             : 1")
    print("Calculator example               : 2")
    print("sum_of_numbers example           : 3")
    print("subtraction_of_numbers example   : 4")
    print("mad_libs example                 : 5")
    print("List example                     : 6")
    print("Tuple example                    : 7")
    print("Function example                 : 8")
    print("Condition example                : 9")
    print("Dictionary example               : 10")
    print("Loop example                     : 11")
    print("Try Except example               : 12")
    print("read file example                : 13")
    print("Class example                    : 14")
    print("String format example            : 15")
    print("rock paper scissor example       : 16")
    print("generate Password example        : 17")
    print("guessing example                 : 18")
    print("palindrome example               : 19")
    print("tic tac toe game                 : 20")
    print("Enumerate Demo                   : 21")
    print("inbuilt function Demo            : 22")
    print("Set example                    : 23")
    choice = int(input("Enter Your choice : "))
    if choice == 0 or choice == 1:
        print_example()
    elif choice == 0 or choice == 2:
        print("========Calculator Example========")
        print(operation())
    elif choice == 0 or choice == 3:
        sum_of_numbers()
    elif choice == 0 or choice == 4:
        subtraction_of_numbers()
    elif choice == 0 or choice == 5:
        mad_libs()
    elif choice == 0 or choice == 6:
        print("========List Example========")
        custom_list()
        custom_list_comprehension()
    elif choice == 0 or choice == 7:
        print("========Tuple Example========")
        custom_tuple()
    elif choice == 0 or choice == 8:
        print("========Function Example========")
        say_hi("kumar", 30)
        print(cube(3))
    elif choice == 0 or choice == 9:
        print("========Condition Example========")
        if_else_gender(False, False)
        print(max_num(3, 5, 4))
    elif choice == 0 or choice == 10:
        print("========Dictionary Example========")
        print(month_names("Dec"))
    elif choice == 0 or choice == 11:
        print("========Loop Example========")
        while_demo()
        for_demo()
    elif choice == 0 or choice == 12:
        print("========Try Except Example========")
        try_except_demo()
    elif choice == 0 or choice == 13:
        print("========read file Example========")
        write_file_demo()
        read_file_demo()
        append_file_demo()
        read_file_demo()
    elif choice == 0 or choice == 14:
        print("========Class Example========")
        class_demo()
    elif choice == 0 or choice == 15:
        print("========String format Example========")
        string_format_demo()
    elif choice == 0 or choice == 16:
        print("======== rock paper scissor Example========")
        play_game()
    elif choice == 0 or choice == 17:
        print("========generate Password Example========")
        print(gen_password(8))
    elif choice == 0 or choice == 18:
        print("========guessing Example========")
        guessing_game()
    elif choice == 0 or choice == 19:
        print("========palindrome Example========")
        palindrome()
    elif choice == 0 or choice == 20:
        print("========tic tac toe========")
        play_tic_tac_toe()
    elif choice == 0 or choice == 21:
        print("========Enumerate Demo========")
        enumerate_demo()
    elif choice == 0 or choice == 22:
        print("========Inbuilt functions Demo========")
        inbuilt_functions_demo()
    elif choice == 0 or choice == 23:
        print("========Set Demo========")
        custom_set()
    else:
        print("Exiting...!!")
