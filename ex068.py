from random import randint

while True:
    jogador = int(input('Informe um valor: '))
    while jogador > 10 or jogador < 0:
        jogador = int(input('Informe um valor: '))

    computador = randint(0, 10)
    total = jogador + computador
    escolha = str(input('Você quer par ou ímpar? [ P / I ] ')).strip().upper()

    print()

    if total % 2 == 0 and escolha == 'P':
        print('=' * 27)
        print('Parabéns, você ganhou da máquina!')
        print(f'O computador escolheu {computador}, e você {jogador}. Total de {total}')
        print('=' * 27)

    elif total % 2 == 1 and escolha == 'I':
        print('=' * 27)
        print('Parabéns, você ganhou da máquina!')
        print(f'O computador escolheu {computador}, e você {jogador}. Total de {total}')
        print('=' * 27)

    else:
        print('=' * 27)
        print('Vish, você perdeu...')
        print('=' * 27)
        break

print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
