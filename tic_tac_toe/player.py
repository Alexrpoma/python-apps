import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> int:
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. input move (0 - 8): ')
            # trying to cast square to integer
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful
            except ValueError:
                print('Invalid Square!, trying again.')
        return value
