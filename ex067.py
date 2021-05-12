print('\033[1m~' * 30)
print('           TABUADA')
print('~\033[m' * 30)

while True:
    print('\033[1;34m=' * 36)
    num = int(input('Deseja ver a tabuada de qual valor?: '))
    if num < 0:
        break
    print('=\033[m' * 36)
    print()
    for contador in range(1, 11):
        print(f'{num} x {contador} = {num * contador}')
    print()
