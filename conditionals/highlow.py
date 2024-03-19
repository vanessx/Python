n1 = int(input('First number: '))
n2 = int(input('Second number: '))
n3 = int(input('Third number: '))

smallest = n1 # atribuir n1 como o menor no inicio para poupar uma linha de código

if n2 < n1 and n2 < n3:
    smallest = n2
elif n3 < n1 and n3 < n2:
    smallest = n3

largest = n1

if n2 > n1 and n2 > n3:
    largest = n2
elif n3 > n1 and n3 > n2:
    largest = n3

print(f'The smallest number is {smallest} and the largest number is {largest}.')
