films = {
    'name': 'dune 2',
    'actress': 'léa seydoux',
    'year': 2024,
}

print(films.values())
print(films.keys())
print(films.items())

for k, v in films.items():
    print(f'The {k} is {v}.')