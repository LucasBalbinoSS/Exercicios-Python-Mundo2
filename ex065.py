num = int(input('Digite um número: '))
continuar = str(input('Deseja continuar?: ')).strip().upper()
soma = num
contador = 1
menor = num
maior = num

while continuar == 'S':
    print()
    num = int(input('Digite um número: '))

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    soma += num
    contador += 1
    continuar = str(input('Quer continuar? [ S / N ] : ')).strip().upper()

print()
print('\033[1mA \033[1;31mmédia\033[m entre todos os valores digitados é igual a \033[1;4;31m%.1f\033[m' % (soma / contador))
print()
print('O \033[1;4;31mmaior número lido\033[m foi o número \033[1;4;31m%i\033[m,' % maior)
print(' e o \033[1;4;31mmenor número lido\033[m foi o número \033[1;4;31m%i\033[m' % menor)
