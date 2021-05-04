m = 0
men = 0
for c in range(1, 6):
    p = float(input('Informe o %i° peso (em Kg): ' % c))
    if c == 1:
        m = p
        men = p
    elif p > m:
        m = p
    elif p < men:
        men = p
print('\033[1;32mO maior peso lido foi de %.2fKg' % m)
print('\033[1;31mO menor peso lido foi de %.2fKg ' % men)
