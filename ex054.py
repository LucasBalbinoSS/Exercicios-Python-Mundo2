from datetime import date as dt

at = dt.today().year
ac = 0
m = 0

for c in range(1, 8):
    nasc = int(input('Informe o ano de nascimento da %i° pessoa: ' % c))
    at2 = at - nasc

    if at2 >= 21:
        ac += 1
    else:
        m += 1
print('De 7 pessoas, %i são maiores de idade\nE %i ainda não são.' % (ac, m))
