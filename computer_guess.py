import random


def computer_guess(max_number):
    low = 1
    high = max_number
    feedback = ''
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high because low = high
        print(f'Is {guess} too high (H), too low (L), or correct (C)?')
        feedback = input('> ').upper()
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
    print(f'Yeah! the computer guessed your number! {guess}')


computer_guess(100)
