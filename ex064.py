print()
print('LEITOR DE NÚMEROS')
print('-' * 25)

num = int(input('Digite um número: '))
soma = 0
contador = 0

while num != 999:
    soma += num
    num = int(input('Digite um número: '))
    contador += 1

print()
print('\033[1;4;34m%i\033[m números \033[4mforam digitados\033[m' % contador)
print('\nE a soma entre esses %i números é igual a: \033[1;4;36m%i' % (contador, soma))
