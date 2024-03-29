from random import randint

count = 1

num = randint(1, 10)  # um número aleatório de 1 a 9
print('-=-' * 20)
guess = int(
    input("Guess the number I'm thinking of, a number beetween 1 and 9: "))
print('-=-' * 20)


while guess != num:
    if num > guess:
        guess = int(input('It is greater! Try again: '))
    else:
        guess = int(input('It is less! Try again: '))
    count += 1


if guess == num:
    print(f'You guessed it! It is {guess}.\nIt took {count} attempts to get it.')

print()
