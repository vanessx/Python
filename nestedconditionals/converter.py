num = int(input('Write a number: '))
type = int(input('Type 1 to convert to \033[34mbinary\033[m\nType 2 to convert to \033[33moctal\033[m\nType 3 to convert to \033[31mhexadecimal\033[m '))

if type == 1:
    c_num = bin(num)
    print(f'The integer {num} in binary is {c_num[2:]}') # 2: é manipulação de string o que indica que só vai mostrar a partir do 2 caracter
elif type == 2:
    c_num = oct(num)
    print(f'The integer {num} in octal is {c_num[2:]}')
elif type == 3:
    c_num = hex(num)
    print(f'The integer in hexadecimal is {c_num[2:]}')
else:
    print('Invalid option. Try again.')
