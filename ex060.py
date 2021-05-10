num = int(input('Informe um número: '))
c = num - 1
conta = num
print('Calculando %i!: ' % num, end='')

while c >= 1:
    print('%i' % c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    conta *= c
    c -= 1
print(conta, end=' ')
print('\033[1;31mFim')
