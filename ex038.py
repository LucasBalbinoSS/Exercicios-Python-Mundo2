n1 = int(input('\033[4;34mInforme um número: '))
n2 = int(input('Informe outro número: '))
print('\033[m\033[1;31mAguarde...')
print()

if n1 > n2:
    print('\033[m\033[32mO número %i é maior que o número %i!' % (n1, n2))
elif n2 > n1:
    print('\033[m\033[32mO número %i é maior que o número %i!' % (n2, n1))
else:
    print('\033[m\033[31mO número %i e o número %i são iguais!' % (n1, n2))
print('\033[1;36mTenha um bom dia!')
