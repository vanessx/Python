from random import randint
from time import sleep

num = randint(1, 9)  # um número aleatório de 1 a 9
print('-=-' * 20)
guess = int(input("Guess the number I'm thinking of, a number beetween 1 and 9: "))
print('-=-' * 20)

print('Loading...')
sleep(3)  # faz o computador esperar 3 segundos antes de executar o próximo comando

if guess == num:
    print(f'You guessed it! It is {guess}.')
else:
    print(f'It is not right... I thought {num} and not {guess}.')

print()
