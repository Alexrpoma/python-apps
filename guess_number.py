import random


def guess_number(max_number):
    random_number = random.randint(1, max_number)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {max_number}: '))
        if guess > random_number:
            print('Sorry the number is high, guess again!')
        elif guess < random_number:
            print('Sorry the number is low, guess again!')
    print(f'You win! you guessed the number {random_number}')


guess_number(10)