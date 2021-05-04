n = int(input('\033[4;1mDigite um número para saber sua tabuada: '))
print()
for c in range(1, 11):
    print('\033[1m\033[m%i x %i = %i' % (n, c, n * c))
print()
print('\033[1mTenha uma boa noite!')
