numbers = []
odd = []
even = []

while True:
    num = int(input('Type a number: '))
    numbers.append(num)
    repeat = input('Do you want to continue? [Y/N]: ').lower()
    if repeat == 'n':
        break

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(numbers)
print(even)
print(odd)
