print("\033[31;100;1mWelcome to PyTicTacToe for 2 players!\033[0m")
print("\033[31;100;1mGrab a friend and let's X-O on!\033[0m")

"""Print the board in neat format."""
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

"""Take player and announce who's turn it is, take position and return X or O on the position's place in the board"""
def ask_choice(board, player):

    while True:
        print("\033[32;1mIt's the turn of player {}.\033[0m".format(player.strip()))
        position = input("Choose position on the board from 1-9: ")
        if len(position) == 1 and position.isnumeric() and position != "0":
            position = int(position) - 1
            if board[position] not in [" X ", " O "]:
                board[position] = player
                return player
            else:
                print("\033[31;1mThis position is taken, try a different cell.\033[0m")
        else:
            print("\033[31;1mYour input is wrong, try again.\033[0m")


"""If the current player is X change it to O and vice versa, return the new value"""
def change_player(player):
    if player == " X ":
        current_player = " O "
        return current_player
    else:
        current_player = " X "
        return current_player


"""Check if the number of X and O is equal to the length of the board and return True"""
def check_if_tie(board):
    if (board.count(" X ") + board.count(" O ")) == len(board):
        return True


"""Take the board and the current player and if the winning condition is fulfilled return the current player"""
def check_for_winner(player, board):
    # perform horizontal check
    if ((board[0] == board[1] == board[2] or
         board[3] == board[4] == board[5] or
         board[6] == board[7] == board[8]) or
            # Perform vertical check
            (board[0] == board[3] == board[6] or
             board[1] == board[4] == board[7] or
             board[2] == board[5] == board[8]) or
            # Perform diagonal check
            (board[0] == board[4] == board[8] or
             board[2] == board[4] == board[6])):
        winner = player

        #if there is no winner the function will return None
        return winner


"Take the board and current player and  if there is a winner or a tie, announce the result."
def check_if_game_over(board, player):

    if check_for_winner(player, board) is not None:
        print("\033[32;100;1mPlayer", player.strip(), "WINS!\033[0m")
        display_board(board)
        return True

    if check_if_tie(board):
        print("\033[32;100;1mITS A TIE!\033[0m")
        return True


"Ask to play again until proper input is given, return True if the user wants to play again, else quit."
def play_again():

    while True:
        print("\033[34;1mWould you like to try again?\033[0m")
        choice = input("\033[34;1mPress Y for YES and N for NO: \033[0m").lower()
        if choice == "y":
            return True

        if choice not in ["y", "n"]:
            print("\033[31;1mWrong input!\033[0m")
            choice

        else:
            print("\033[31;100;1mThank you for playing PyTicTacToe!\033[0m")
            exit()


"""Initialize the board and the starting player, and play until the user decides to quit"""
def main():

    player = " X "
    board = ["_1_", "_2_", "_3_",
             "_4_", "_5_", "_6_",
             "_7_", "_8_", "_9_"]

    while True:
        display_board(board)
        ask_choice(board, player)
        if check_if_game_over(board, player) is True:
            if play_again() is True:
                main()
        player = change_player(player)

main()