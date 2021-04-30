peso = float(input('Informe seu peso em Kg: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura ** 2)

print('Você tem \033[1m%.1f\033[m Kg e \033[1m%.2f\033[m de altura' % (peso, altura))
print('Seu imc é igual a \033[4;1m%.1f\033[m' % imc)

if imc < 18.5:
    print('\033[4;31mAbaixo do peso\033[m\nComa mais! (Produtos saudáveis)')
elif 18.5 <= imc < 25:
    print('\033[4;32mPESO IDEAL\033[m!\nContinue assim!')
elif 25 <= imc < 30:
    print('\033[4;33mSOBREPESO\033[m\nSe cuide mais...')
elif 30 <= imc < 40:
    print('\033[4;31mOBESIDADE\033[m...\nSe cuide mais...')
else:
    print('\033[4;31mOBESIDADE MÓRBIDA\033[m...\nSe cuide mais...')
print('Tenha um bom dia!')
