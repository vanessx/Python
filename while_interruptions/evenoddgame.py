from random import randint

count = 0

while True:
    number = int(input('Number: '))
    even_odd = input('Even or Odd? ').lower()
    computer = randint(1, 10)
    sum = number + computer
    if sum % 2 == 0 and even_odd == 'even':
        print(f'The sum of {number} and {computer} is {sum}. You won!')
        count += 1
    elif sum % 2 != 0 and even_odd == 'odd':
        print(f'The sum of {number} and {computer} is {sum}. You won!')
        count += 1
    else:
        print(f'The sum of {number} and {computer} is {sum}. You lost!')
        break

print(f'You won {count} times.')