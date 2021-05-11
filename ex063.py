print('=-' * 8)
print('   FIBONACCI')
print('=-' * 8)

qttermos = int(input('Quantos termos você deseja ver?: '))
contador = 3
termo1 = 0
termo2 = 1

print('~' * 30)
print('%i - %i' % (termo1, termo2), end='')

while contador <= qttermos:
    termo3 = termo1 + termo2
    print(' - %i' % termo3, end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' \033[1;31;4mFIM\033[m')
print('~' * 30)
