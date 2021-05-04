
soma = 0  #SOMA DA IDADE DO GRUPO.
media = 0  #MEDIA DE IDADE DO GRUPO.
mv = 0  #MAIS VELHO.
qm20 = 0  #QUANTIDADE DE MULHERES MENOS DE 20 ANOS.
nomevelho = '' #NOME HOMEM MAIS VELHO.

for c in range(1, 5):
    print('\033[37;1m----\033[m \033[1m%i° Usuário \033[1;37m----' % c)
    nome = str(input('\033[mInforme seu primeiro nome: ')).strip().title()
    print()
    Nn = nome.split()
    print('Olá \033[1;4m%s\033[m!' % Nn[0])
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo (M/F): ')).upper().strip()
    soma += idade

    if c == 1 and sexo == 'M':
        mv = idade
        nomevelho = nome
    elif sexo == 'M' and idade > mv:
        mv = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        qm20 += 1

    print()
media = soma / 4
print('A média de idade do grupo é de %.1f' % media)
print('O homem mais velho tem %i anos e se chama %s' % (mv, nomevelho))
print('Ao todo, são %i mulheres com menos de 20 anos' % qm20)
