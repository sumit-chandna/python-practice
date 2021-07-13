empty_char = ' '
board = [
    [empty_char, empty_char, empty_char],
    [empty_char, empty_char, empty_char],
    [empty_char, empty_char, empty_char]
]
valid_range = [1, 2, 3]


def display():
    print("============================================")
    for row in board:
        print(row)
    print("============================================")


def play_board_game():
    display()
    current_character = 'X'
    player_number = 1
    player_won = False
    while can_continue(player_won):
        print(f"Player : player{player_number}, Current character : {current_character}")
        position_row = user_input(f"Enter the row[valid range : {valid_range}]: ")
        position_index = user_input(f"Enter the index position[valid range : {valid_range}]: ")
        if board[position_row][position_index] != empty_char:
            print("invalid position..!! already used")
        else:
            board[position_row][position_index] = current_character
            if check_win_condition(current_character):
                print(f"Player player{player_number} Won with {current_character}")
                player_won = True
            if current_character == 'X':
                current_character = 'O'
                player_number = 2
            else:
                current_character = 'X'
                player_number = 1
            display()


def check_win_condition(current_character):
    # row check
    for row in range(0, 3):
        if board[row].count(current_character) == 3:
            return True
    # column check
    for column in range(0, 3):
        if board[0][column] == board[1][column] == board[2][column] == current_character:
            return True
    # diagonal check
    if board[0][0] == board[1][1] == board[2][2] == current_character \
            or board[0][2] == board[1][1] == board[2][0] == current_character:
        return True
    return False


def can_continue(player_won):
    if player_won:
        return False
    for row in board:
        if empty_char in row:
            return True
    return False


def user_input(msg):
    choice = 'Wrong'
    within_range = False
    while choice.isdigit() is False or within_range is False:
        choice = input(msg)
        if choice.isdigit() and int(choice) in valid_range:
            within_range = True
        else:
            print("Invalid option")
    return int(choice) - 1
