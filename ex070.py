print('=-' * 20)
print(' ' * 10, 'LOJA BALBINO')
print('=-' * 20)
print()

soma = 0.0
contador = 0
menorpreco = 0.0
nomemenorpreco = ''


while True:
    nomeproduto = str(input('Informe o nome do produto: ')).strip().title()
    precoproduto = float(input('Informe o preço do produto: R$ '))
    if precoproduto > 1000:
        contador += 1
    elif precoproduto < menorpreco:
        nomemenorpreco = nomeproduto
        menorpreco += precoproduto
    soma += precoproduto

    continuar = str(input('Quer continuar? [ S / N ]: ')).strip().upper()
    if continuar == 'N':
        break
    while continuar != 'S':
        continuar = str(input('Quer continuar? [ S / N ]: ')).strip().upper()
    print('=-' * 20)

print(f'O total gasto nessa compra foi de R${soma}')
print(f'Você comprou {contador} produtos que custam mais de R$1000.00')
print(f'O produto mais barato que foi coprado foi {nomemenorpreco}, e custa R${menorpreco}')
