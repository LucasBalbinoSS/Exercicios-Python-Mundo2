import time as tm
n = int(input('Digite um número inteiro: '))

tm.sleep(0.5)
print('Aguarde..')
print()
tm.sleep(0.5)

print('''Escolha uma das opções abaixo para conversão:
[ \033[1;35m1\033[m ] converter para \033[1mBINÁRIO\033[m
[ \033[1;35m2\033[m ] converter para \033[1mOCTAL\033[m
[ \033[1;35m3\033[m ] converter para \033[1mHEXADECIMAL\033[m''')
print()

op = int(input('Sua opção: '))

if op == 1:
    print('\033[1;32mO número {}, convertido para binário, se torna {}'.format(n, bin(n)[2:]))
    print('\033[mTenha um bom dia!')
elif op == 2:
    print('\033[1;32mO número {}, convertido para octal, se torna {}'.format(n, oct(n)[2:]))
    print('\033[mTenha um bom dia!')
elif op == 3:
    print('\033[1;32mO número {}, convertido para hexadecimal, se torna{}'.format(n, hex(n)[2:]))
    print('\033[mTenha um bom dia!')
else:
    print('\033[31mOpção inválida!\033[m')
    print('Hm...')
