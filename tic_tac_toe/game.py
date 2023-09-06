from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        # we'll use a single list to rep 3x3 board, range(9) -> 0 to 8
        self.board = [' ' for _ in range(9)]  # -> [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # keep track of winner.
        self.current_winner = None

    def print_board(self):
        # Getting rows
        # if i = 0 -> board[0:3] we select just a part of the array -> [0, 1, 2]
        rows = [self.board[i * 3: (i + 1) * 3] for i in range(3)] # -> [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        for row in rows:
            print('| ' + ' | '.join(row) + ' |')
            # It will print:
            # |   |   |   |
            # |   |   |   |
            # |   |   |   |

    @staticmethod
    def print_board_nums() -> None:
        # number_board -> [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print(number_board)
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            # It will print:
            # | 0 | 1 | 2 |
            # | 3 | 4 | 5 |
            # | 6 | 7 | 8 |

    def available_moves(self) -> list:
        # i -> index, spot -> an element of the array (board)
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self) -> bool:
        return ' ' in self.board

    def num_empty_squares(self) -> int:
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, make the move (assign letter('X' or 'O') to square)
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere. we have to check all of these!

        # check the rows
        row_ind = square // 3
        row = self.board[(row_ind * 3): (row_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True

        # check columns
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        # (0, 4, 8) or (2, 4, 6)
        if square % 2 == 0:
            diagonal_right = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_right]):
                return  True
            diagonal_left = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_left]):
                return True

        # if all of there fail
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X'  # starting letter

    # Iterate while in the board exist empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter, f'makes a move to square {square}')
                game.print_board()
                print('')  # empty line
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            # after we made a move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'  # switches player

    if print_game:
        print('It\'s a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
