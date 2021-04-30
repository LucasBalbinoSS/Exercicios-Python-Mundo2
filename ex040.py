nome_professor = str(input('NOME PROFESSOR(A): ')).strip().upper()

print('Aguarde...')

nome = str(input('Informe o nome do aluno: ')).strip().title()
nota1 = float(input('Informe a 1°a nota: '))
nota2 = float(input('Informe a 2°a nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print()
    print('O aluno \033[1;36m%s\033[m foi \033[1;4;31mREPROVADO\033[m!' % nome)
    print('Sua média foi de %.2f' % media)
elif media == 5 or media <= 6.9:
    print()
    print('O aluno \033[1;36m%s\033[m está de \033[1;4;33mRECUPERAÇÃO\033[m!' % nome)
    print('Sua média foi de %.2f' % media)
elif media >= 7:
    print()
    print('O aluno \033[1;36m%s\033[m foi \033[1;4;32mAPROVADO!' % nome)
    print('Sua média foi de %.2f' % media)
print()
print('\033[mTenha um bom dia professor(a) %s!' % nome_professor)
