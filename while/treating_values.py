count = sum = 0
number = int(input('Number: '))

while number != 999:
    count += 1
    sum += number
    number = int(input('Number: '))
        
print(f'The count of numbers you type is {count} and the sum is {sum}.')