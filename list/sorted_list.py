numbers = []

for num in range(0,5):
    number = int(input('Type a number: '))
    if num == 0 or number > numbers[-1]:
        numbers.append(number)
    else:
        place = 0
        while place < len(numbers): # se a posição for menor que o total de posições na lista
            if number <= numbers[place]: 
                numbers.insert(place, number)
                break
            place += 1

print('The numbers on the list are:')
for number in numbers:
    print(number, end=' ')