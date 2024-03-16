import math

c1 = float(input('First cateto: '))
c2 = float(input('Second cateto: '))
hypotenuse = math.sqrt(math.pow(c1, 2) + math.pow(c2, 2))  # mais fácil seria hypotenuse = math.hypot(c1, c2)

print(f'The hypotenuse is {hypotenuse:.2f}cm')
