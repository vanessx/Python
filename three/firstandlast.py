x = input('Write something: ').upper().strip()
print(x.count('A'))
print(x.find('A') + 1) # toda a contagem começa do zero
print(x.rfind('A') + 1) # conta a partir do lado direito 