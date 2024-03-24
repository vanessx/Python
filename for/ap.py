term = int(input('First term: '))
ratio = int(input('Ratio: '))
tenth = term + 10 * ratio # eu quero que mostre os primeiros 10 termos, se eu quisesse 15 colocava 15 e por aí...

for c in range(term, tenth, ratio):
    print(c, end=' ')
