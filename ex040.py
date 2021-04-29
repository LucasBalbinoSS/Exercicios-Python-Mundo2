import time as tm
nome_professor = str(input('NOME PROFESSOR(A): ')).strip().upper()
tm.sleep(1)
print('Aguarde...')
tm.sleep(1)

nome = str(input('Informe o nome do aluno: ')).strip().title()
nota1 = float(input('Informe a 1°a nota: '))
nota2 = float(input('Informe a 2°a nota: '))
media = (nota1 + nota2) / 2
tm.sleep(1)

if media < 5:
    print()
    print('O aluno \033[1;36m%s\033[m foi \033[1;4;31mREPROVADO\033[m!' % nome)
elif media == 5 and media <= 6.9:
    print()
    print('O aluno \033[1;36m%s\033[m está de \033[1;4;33mRECUPERAÇÃO\033[m!' % nome)
elif media >= 7:
    print()
    print('O aluno \033[1;36m%s\033[m foi \033[1;4;32mAPROVADO!' % nome)
print()
print('\033[mTenha um bom dia professor(a) %s!' % nome_professor)