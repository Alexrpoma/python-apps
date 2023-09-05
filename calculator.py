print('Welcome to python calculator!')
print('What king of operation you wish?')


def show_menu():
    print('1. Sum')
    print('2. Rest')
    print('3. Multiplication')
    print('4. Division')
    print('Select an option:')


show_menu()


def get_number():
    while True:
        data = input('> ')
        if data.isnumeric():
            break
        print('\nThe data must be a number!')
    return int(data)


option = get_number()
print('Enter the first number:')
number0 = get_number()
print('Enter the second number:')
number1 = get_number()


def sum_numbers(a, b):
    return a + b


def rest(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


if option == 1:
    print(f'The sum of them are: {sum_numbers(number0, number1)}')
elif option == 2:
    print(f'The rest of them are: {rest(number0, number1)}')
elif option == 3:
    print(f'The multiply of them are: {multiplication(number0, number1)}')
elif option == 4:
    print(f'The sum of them are: {division(number0, number1)}')
else:
    print('Invalid option!')
