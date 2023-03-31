from random import randint
"""Get number from user.

Try until user gives a proper number.

:rtype: None
"""

guess = False
number = randint(1, 100)

while guess != number:
    try:
        guess = int(input('Enter the number: '))
        guess = int(guess)

        if guess < number:
            print('Too small!')
        elif guess > number:
            print('too big!')
        else:
            print('You win!')
    except ValueError:
        print('That is not a number!')
        continue
