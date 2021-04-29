from datetime import date as dt

aat = dt.today().year
an = int(input('Informe o ANO DE NASCIMENTO do atleta: '))
idade = aat - an

if idade <= 0:
    print('ERRO')
elif idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JÚNIOR')
elif idade <= 25:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')
print('\033[mTenha um bom dia!')
