import random


def play():
    print("'r' for Rock, 'p' for paper, 's' for scissors")
    user = input("> ").lower()
    computer = random.choice(['r', 'p', 's'])
    print(f'You have chosen {user} and the computer have chosen {computer}')
    if user == computer:
        print('It\'s a tie!')
    elif is_win(user, computer):
        print('You Won!')
    else:
        print('You lost!')


def is_win(player, opponent) -> bool:
    # return true if player wins
    if ((player == 'r' and opponent == 's') or
            (player == 'p' and opponent == 's') or
            (player == 's' and opponent == 'p')):
        return True
    return False


play()
