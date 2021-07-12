def get_player_choice(count):
    player_input = input("Player " + str(count) + " :: Enter Your choice(Rock/Paper/Scissors): ")
    while player_input.lower() != "rock" and player_input.lower() != "paper" and player_input.lower() != "scissors":
        player_input = input("Player " + str(count) + " :: Enter Your choice Again(Rock/Paper/Scissors): ")
    return player_input


def game_rules(player1_choice, player2_choice):
    if (player1_choice.lower() == "rock" and player2_choice.lower() == "scissors") or (
            player1_choice.lower() == "scissors" and player2_choice.lower() == "rock"):
        print("Rock Beats Scissors")
    elif (player1_choice.lower() == "scissors" and player2_choice.lower() == "paper") or (
            player1_choice.lower() == "paper" and player2_choice.lower() == "scissors"):
        print("Scissors beats paper")
    elif (player1_choice.lower() == "paper" and player2_choice.lower() == "rock") or (
            player1_choice.lower() == "rock" and player2_choice.lower() == "paper"):
        print("Paper beats rock")
    else:
        print("No Result")


def play_game():
    re_run = True
    while re_run:
        player1_input = get_player_choice(1)
        player2_input = get_player_choice(2)
        game_rules(player1_input, player2_input)
        play_again = input("Want To play Again (Y/N): ")
        if play_again == "Y":
            re_run = True
        else:
            re_run = False
            print("Game Ends...!!")