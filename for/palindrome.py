phrase = input('Write a phrase: ').strip().lower().replace(' ', '')

if phrase == phrase[:: -1]:  # -1 quer dizer que volta para trás
    print('It is a polindrome.')
else:
    print('It is not a polindrome.')


# se usasse um loop for
"""
for c in range(len(phrase) -1, -1. -1):
"""
