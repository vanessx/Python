higher = 0
lower = 0

for w in range(1, 6):
    weight = float(input(f'What is the weight of the {w}° person: '))
    if w == 1: # atribui ao primeiro valor o maior e o menor
        higher = weight
        lower = weight
    else:
        if weight > higher:
            higher = weight
        if weight < lower:
            lower = weight

print(f'The highest weight is {higher:.1f}kg and the lowest is {lower:.1f}kg.')
