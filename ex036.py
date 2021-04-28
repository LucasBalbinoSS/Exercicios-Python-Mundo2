nome = str(input('Por favor, informe seu nome: ')).strip().title()
valorC = float(input('Informe o valor da casa: R$'))
sal = float(input('Informe sua renda salarial: R$'))
a = int(input('Em quantos anos você planeja quitar a casa?: '))

p = valorC / (a * 12)  #Prestação
m = sal * 30 / 100     #Mínimo

print()
print('\033[31mATENÇÃO!\033[m %s\nPara pagar uma casa de %.2f, em %i anos\nA prestação será de R$%.2f' % (nome, valorC, a, p))
print()

if p <= min:
    print('Empréstimo \033[32mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[31mNEGADO\033[m!')
