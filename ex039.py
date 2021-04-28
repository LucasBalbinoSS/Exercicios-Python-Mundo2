from datetime import date as dt
import time as tm

nome = str(input('Informe seu nome: ')).strip()
ano = int(input('Informe o ano de seu nascimento: '))
a = dt.today().year - ano
f = 18 - a

print('-' * 37)
print('Prazer, \033[1m%s\033[m!\nSuas informações estão logo abaixo.' % nome)
tm.sleep(2.5)
print()
print('Aguarde...')
tm.sleep(1.7)

if a < 18:
    print()
    print('Você tem \033[1;32m%i \033[mano(s).\n\033[1;32mFaltam %i ano(s) para seu alistamento.\033[m' % (a, f))
elif a == 18:
    print()
    print('Você tem \033[1;33m%i \033[manos.\n\033[1;33mEstá na hora de fazer seu alistamento.\033[m\nEntre no site www.brasilalistamento.com para obter mais informações.' % a)
elif a > 18:
    print()
    print('Você tem \033[1;31m%i \033[manos.\033[1;31m\nVocê já deveria ter feito seu alistamento.\033[m\nEntre no site www.brasilalistamento.com para obter mais informações.' % a)
print('-' * 37)
print('Tenha um bom dia!')
