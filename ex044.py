print('{:^40}'.format(' \033[1;4;35mLOJAS BALBINO\033[m '))
print()

preco = float(input('Informe o preço do produto: R$'))

print('''Qual será a condição de pagamento?
[ 1 ] Dinheiro/cheque (\033[4;1mà vista\033[m)
[ 2 ] Cartão (\033[4;1mà vista\033[m)
[ 3 ] Até \033[4;1m2x no cartão\033[m
[ 4 ] \033[4;1m3x ou mais\033[m no cartão''')

print()
escolha = int(input('Escolha: '))

if escolha == 1:
    pag = int(input('[ 1 ]Dinheiro ou [ 2 ]Cheque?: '))
    if pag == 1:
        print('O valor de R$\033[1;4;32m{:.2f}\033[m com o pagamento '.format(preco,), end='')
        print(' a vista com \033[1;34mDINHEIRO\033[m,', end='')
        print(' se torna R$\033[1;4;32m{:.2f}\033[m com 10% de desconto'.format(preco - (preco * 10 / 100)))
    elif pag == 2:
        print('O valor de R$\033[1;4;32m{:.2f}\033[m com o pagamento '.format(preco,), end='')
        print(' a vista com \033[34;1mCHEQUE\033[m,', end='')
        print(' se torna R$\033[1;4;32m{:.2f}\033[m com 10% de desconto'.format(preco - (preco * 10 / 100)))
    else:
        print()
        print('\033[1;4;31mERRO, TENTE NOVAMENTE\033[m')
elif escolha == 2:
    print('O valor de R$\033[1;4;32m{:.2f}\033[m,'.format(preco, ), end='')
    print(' com o pagamento em cartão, se torna R$\033[1;4;32m{:.2f}\033[m'.format(preco - (preco * 5 / 100)))
elif escolha == 3:
    pag = int(input('Deseja pagar em 1 ou 2 vezes?: '))
    if pag == 1:
        print('Valor à pagar: R$\033[1;4;32m{:.2f}\033[m'.format(preco))
    elif pag == 2:
        print('Para quitar o valor de R$\033[1;4;32m{:.2f}\033[m em duas prestações,'.format(preco), end='')
        print(' você terá que pagar DUAS parcelas de R$\033[1;4;32m{:.2f}\033[m'.format(preco / 2))
    else:
        print('\033[1;4;31mERRO, TENTE NOVAMENTE\033[m')
elif escolha == 4:
    p20 = preco * 20 / 100
    pag = int(input('Você deseja pagar o valor de R$\033[1;4;32m{:.2f}\033[m em quantas vezes?: '.format(preco + p20)))
    print('Para quitar o valor de R$\033[1;4;32m{:.2f}\033[m em {} prestações,'.format(preco + p20, pag), end='')
    print(' você terá que pagar {} parcelas de R$\033[1;4;32m{:.2f}\033[m COM JUROS'.format(pag, (preco + p20) / pag))
else:
    print('\033[1;4;31mERRO, TENTE NOVAMENTE')
