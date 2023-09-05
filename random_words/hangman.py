import random
import string
from hangman_visual import lives_visual_dict
from words_list import words


def get_word() -> str:
    return random.choice(words)


def hangman():
    print('Welcome to hangman game!')
    word = get_word().upper()
    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(letters) > 0 and lives > 0:
        print(f'You have {lives} lives left and you have used these letters: ', ' '.join(used_letters).upper())
        current_word = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(current_word))
        print('Guess a letter:')
        input_letter = input('> ').upper()
        if input_letter in alphabet - used_letters:
            used_letters.add(input_letter)
            if input_letter in letters:
                letters.remove(input_letter)
            else:
                print('Wrong!')
                lives -= 1
        elif input_letter in used_letters:
            print(f'You have used the letter {input_letter}, guess another letter.')
        else:
            print('Invalid letter')
    if len(letters) == 0 and lives > 0:
        print(lives_visual_dict[lives])
        print(f'You won! The word is {word}')
    else:
        print(f'You lost, the letter was {word}')


hangman()
