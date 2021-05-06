sexo = 'K'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[1;4mInforme seu sexo [ M / F ]\033[m: ')).upper().strip()
if sexo == 'M':
    print()
    print('Seu sexo é \033[4;31mMASCULINO\033[m\nTenha uma boa noite moço!')
elif sexo == 'F':
    print()
    print('Seu sexo é \033[4;31mFEMININO\033[m\nTenha uma boa noite moça!')
