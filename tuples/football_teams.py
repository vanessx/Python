teams = ('sporting', 'benfica', 'porto', 'braga', 'vitória SC', 'moreirense',
         'arouca', 'famalicão', 'casa pia', 'farense', 'boavista', 'rio ave',
         'estoril', 'gil vicente', 'estrela amadora', 'portimonense', 'vizela',
         'chaves')

print('\033[4mThe top5 is:\033[m')
for team in teams[0:5]:
    print(team.title())

print('\n\033[4mThe last 4 are:\033[m')
for team in teams[-4:]:
    print(team.title())

print('\n\033[4mThe teams in alphabetical order:\033[m')
for team in sorted(teams):
    print(team.title())

for pos, team in enumerate(teams):
    if team == 'porto':
        print(f'\n{team.title()} is in position {pos + 1}.')
        