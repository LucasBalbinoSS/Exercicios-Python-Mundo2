print('=-' * 20)
print(' ' * 10, 'LOJA BALBINO')
print('=-' * 20)
print()

soma = contador = totmil = menorpreco = 0
nomemenorpreco = ' '

while True:
    nomeproduto = str(input('Informe o nome do produto: ')).strip().title()
    precoproduto = float(input('Informe o preço do produto: R$ '))
    contador += 1
    if precoproduto > 1000:
        totmil += 1

    soma += precoproduto

    if contador == 1 or precoproduto < menorpreco:
        menorpreco = precoproduto
        nomemenorpreco = nomeproduto

    continuar = str(input('Quer continuar? [ S / N ]: ')).strip().upper()
    if continuar == 'N':
        break
    while continuar != 'S':
        continuar = str(input('Quer continuar? [ S / N ]: ')).strip().upper()
    print('=-' * 20)
print()
print('TOTAL DA COMPRA')
print()
print(f'O total gasto nessa compra foi de R${soma}')
print(f'Você comprou {totmil} produtos que custam mais de R$1000.00')
print(f'O produto mais barato que foi coprado foi {nomemenorpreco}, e custa R${menorpreco}')
