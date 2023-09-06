class TicTacToe:
    def __init__(self):
        # we'll use a single list to rep 3x3 board, range(9) -> 0 to 8
        self.board = [' ' for _ in range(9)]  # -> [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # keep track of winner.
        self.current_winner = None

    def print_board(self):
        # Getting rows
        # if i = 0 -> board[0:3] we select just a part of the array -> [0, 1, 2]
        rows = [self.board[i * 3: (i + 1) * 3] for i in
                range(3)]  # -> [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        for row in rows:
            print('| ' + ' | '.join(row) + ' |')
            # It will print:
            # |   |   |   |
            # |   |   |   |
            # |   |   |   |

    @staticmethod
    def print_board_nums():
        # number_board -> [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print(number_board)
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            # It will print:
            # | 0 | 1 | 2 |
            # | 3 | 4 | 5 |
            # | 6 | 7 | 8 |

    def available_moves(self):
        # i -> index, spot -> an element of the array (board)
        return [i for i, spot in enumerate(self.board) if spot == ' ']
