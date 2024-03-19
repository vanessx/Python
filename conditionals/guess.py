from random import randint
num = randint(1, 9)
guess = int(input('Guess the number I chose: '))

if guess == num:
    print('You guessed it!')
else:
    print('It is not right...')
