from random import randint


def guess_the_nuber():
    """Get number from user.

    Try until user gives a proper number.

    :return: None
    """

    guess = False
    number = randint(1, 100)

    while guess != number:
        try:
            guess = int(input('Enter the number: '))

            if guess < number:
                print('Too small!')
            elif guess > number:
                print('too big!')
            else:
                print('You win!')
        except ValueError:
            print('That is not a number!')
            continue


guess_the_nuber()
