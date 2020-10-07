from Models import Player, Board
from Views import View

class GameController:

    def __init__(self, board, view):
        self.board = board
        self.current_player = self.board.player1.symbol
        self.winner = None
        self.view = view

    def display_board(self):
        self.view.display_board(self.board)

    def handle_choice(self):

        """Take player and announce who's turn it is, take position and return X or O on the position's place in the
        board """

        while True:

            View().announce_player(self.current_player)
            position = View.ask_choice(self)
            if len(position) == 1 and position.isnumeric() and position != "0":
                position = int(position) - 1
                if self.board.cells[position] not in [1, 2]:
                    if self.current_player == self.board.player1.symbol:
                        self.board.cells[position] = 1
                        break
                    else:
                        self.board.cells[position] = 2
                        break
                else:
                    View().place_taken()
            else:
                View().wrong_input()

    def change_player(self):

        """If the current player is X change it to O and vice versa, return the new value"""

        if self.current_player == self.board.player1.symbol:
            self.current_player = self.board.player2.symbol

        else:
            self.current_player = self.board.player1.symbol

    def check_if_tie(self):

        """Check if the number of X and O is equal to the length of the board and return True"""

        if (self.board.cells.count(1) + self.board.cells.count(2)) == len(self.board.cells):
            self.winner = "Tie"
            self.display_board()
            View().announce_result(self.winner)

    def check_for_winner(self):

        """Take the board and the current player and if the winning condition is fulfilled return the current player"""

        # Perform horizontal check
        if ((self.board.cells[0] == self.board.cells[1] == self.board.cells[2] != 0 or
             self.board.cells[3] == self.board.cells[4] == self.board.cells[5] != 0 or
             self.board.cells[6] == self.board.cells[7] == self.board.cells[8] != 0) or
                # Perform vertical check
                (self.board.cells[0] == self.board.cells[3] == self.board.cells[6] != 0 or
                 self.board.cells == self.board.cells[4] == self.board.cells[7] != 0 or
                 self.board.cells[2] == self.board.cells[5] == self.board.cells[8] != 0) or
                # Perform diagonal check
                (self.board.cells[0] == self.board.cells[4] == self.board.cells[8] != 0 or
                 self.board.cells[2] == self.board.cells[4] == self.board.cells[6] != 0)):
            self.winner = self.current_player
            self.display_board()
            View().announce_result(self.winner)

    def play_again(self):
        if self.winner is not None:

            restart = input("Would you like to go for another round?\nInsert Y for YES and N for NO: ")

            if restart.lower() == "y":
                self.winner = None
                return True
            elif restart.lower() == "n":
                print("Thank you for playing PyTicTacToe!")
                return False
            else:
                self.play_again()