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

choice_count = 0
if __name__ == '__main__':
    print("all example                      : " + str(choice_count))
    choice_count += 1
    print("print format example             : " + str(choice_count))
    choice_count += 1
    print("Calculator example               : " + str(choice_count))
    choice_count += 1
    print("sum_of_numbers example           : " + str(choice_count))
    choice_count += 1
    print("subtraction_of_numbers example   : " + str(choice_count))
    choice_count += 1
    print("mad_libs example                 : " + str(choice_count))
    choice_count += 1
    print("List example                     : " + str(choice_count))
    choice_count += 1
    print("Tuple example                    : " + str(choice_count))
    choice_count += 1
    print("Function example                 : " + str(choice_count))
    choice_count += 1
    print("Condition example                : " + str(choice_count))
    choice_count += 1
    print("Dictionary example               : " + str(choice_count))
    choice_count += 1
    print("Loop example                     : " + str(choice_count))
    choice_count += 1
    print("Try Except example               : " + str(choice_count))
    choice_count += 1
    print("read file example                : " + str(choice_count))
    choice_count += 1
    print("Class example                    : " + str(choice_count))
    choice_count += 1
    print("String format example            : " + str(choice_count))
    choice_count += 1
    print("rock paper scissor example       : " + str(choice_count))
    choice_count += 1
    print("generate Password example        : " + str(choice_count))
    choice_count += 1
    print("guessing example                 : " + str(choice_count))
    choice_count += 1
    print("palindrome example               : " + str(choice_count))
    choice_count += 1
    print("tic tac toe game                 : " + str(choice_count))
    choice_count += 1
    print("Enumerate Demo                   : " + str(choice_count))
    choice_count += 1
    print("inbuilt function Demo            : " + str(choice_count))
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
    else:
        print("Exiting...!!")
