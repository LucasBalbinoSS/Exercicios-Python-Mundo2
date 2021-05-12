soma = 0
contador = 0

while True:
    num = int(input('Digite um número (\033[1;31m999\033[m para \033[4mencerrar\033[m o programa): '))
    if num == 999:
        break
    soma += num
    contador += 1

print(f'Foram digitados {contador} números, e a soma de todos esses {contador} é igual a {soma}.')
