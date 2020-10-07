class View:

    def display_board(self, board):

        """Takes qn instance of board.
         Works on array to iterate through and symbols for player1 and player2 - strings
         If it is the third element of the row, starts from new line, otherwise separates items with |.
         Player1's choices are represented by 1, player2's choices respectively by 2, free spots are by 0."""

        for i in range(1, len(board.cells) + 1):
            if board.cells[i-1] == 0:
                print(f"_{i}_", end="\n" if i % 3 == 0 else " | ")
            if board.cells[i-1] == 1:
                print(" "+board.player1.symbol+" ", end="\n" if i % 3 == 0 else " | ")
            if board.cells[i-1] == 2:
                print(" "+board.player2.symbol+" ", end="\n" if i % 3 == 0 else " | ")

    def ask_choice(self):

        position = input("Please choose your position: ")
        return position

    def announce_result(self, winner):

        if winner == "Tie":
            print("\033[32;100;1mITS A TIE!\033[0m")
        else:
            print("\033[32;100;1mPlayer", winner, "WINS!\033[0m")

    def announce_player(self, player):
        print("\033[32;1mIt's the turn of player {}.\033[0m".format(player.strip()))

    def place_taken(self):
        print("\033[31;1mThis position is taken, try a different cell.\033[0m")

    def wrong_input(self):
        print("\033[31;1mYour input is wrong, try again.\033[0m")
