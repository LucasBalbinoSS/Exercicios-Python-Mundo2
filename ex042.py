r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print()
        print('Os segmentos acima PODEM formar um triângulo \033[34mEQUILÁTERO\033[m!!!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print()
        print('Os segmentos acima PODEM formar um triângulo \033[34mESCALENO\033[m!!!')
    else:
        print()
        print('Os seguimentos acima PODEM formar um triângulo \033[34mISÓCELES\033[m!!! ')
else:
    print()
    print('\033[1;31mOs segmentos acima NÃO PODEM formar um triângulo...')
print('\033[mTenha um bom dia!')
