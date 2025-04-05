import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print('guess the number from 1 to 100')

    while True:
        guess = int(input('your number: '))
        attempts += 1

        if guess < number_to_guess:
            print('>> its wrong, my number is higher')
        elif guess > number_to_guess:
            print('>> its wrong, my number is lower')
        else:
            print(f'>> You WON!! attempts: {attempts}')
            break;

if __name__ == '__main__':
    guess_number()
