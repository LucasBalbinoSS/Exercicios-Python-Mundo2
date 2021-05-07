num = int(input('Informe um número: '))
c = num - 1
conta = num

while c >= 1:
    print('%i! = %i x %i ' % (num, num, c), end='')
    conta *= c
    c -= 1
print(conta)
print()
print('Fim')