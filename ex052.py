n = int(input('Informe um número: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('%i ' % c, end='')
print('\n\033[mO número %i foi devisível %i vezes' % (n, tot))

if tot == 2:
    print('Então, ele é um número primo!')
else:
    print('Então, ele não é primo...')
