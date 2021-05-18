contmais18idade = 0
conthomens = 0
contmulheresmen20 = 0
continuar = 'S'

while True:
    print('\033[m=-\033[m' * 17)
    idade = int(input('Informe a sua idade: '))
    if idade > 18:
        contmais18idade += 1

    sexo = str(input('Informe seu sexo [ M / F ]: ')).strip().upper()
    if sexo == 'F' and idade < 20:
        contmulheresmen20 += 1
    if sexo == 'M':
        conthomens += 1

    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Informe seu sexo [ M / F ]: ')).strip().upper()
    print('\033[m=-\033[m' * 17)

    continuar = str(input('Quer continuar? [ S / N ]: ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S / N ]: ')).strip().upper()

    if continuar == 'N':
        break

print('=-' * 20)
print(' ' * 10, '\033[4;1;37mResultado da análise\033[m')
print()
print(f'\033[1;4m{contmais18idade}\033[m pessoas tem mais de 18 anos.')
print(f'\033[1;4m{conthomens}\033[m dos cadastrados são homens.')
print(f'\033[1;4m{contmulheresmen20}\033[m dos cadastrados', end='')
print(f' são mulheres e tem mais de 20 anos.')
print('=-' * 20)
