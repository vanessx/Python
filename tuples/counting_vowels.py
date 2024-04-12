people = ('lea', 'rosamund', 'margot', 'paul', 'tom', 'josey', 'anya',
          'daisy', 'amber', 'nathalie', 'niek', 'floor', 'loreen')

for person in people:
    print(f'\nIn the word {person.upper()} we have', end=' ')
    for letter in person:
        if letter.lower() in 'aeiou':
            print(f'{letter}', end=' ')