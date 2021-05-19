print('=' * 30)
print('{:^30}'.format('BANCO LUCAS'))
print('=' * 30)
valor = int(input('Informe o valor a ser sacado: '))
total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif total == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break

print('=' * 35)
print('Volte sempre ao BANCO LUCAS, bom dia!')