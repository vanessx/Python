count = sum = 0

while True:
    number = int(input('Number: '))
    if number == 999:
        break
    count += 1
    sum += number

print(f'The total of numbers are {count}.\nThe sum is {sum}.')