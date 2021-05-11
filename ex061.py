primeiro = int(input('Informe o primeiro termo (de onde a progressão começará): '))
razão = int(input('Informe a razão: '))
termo = primeiro
c = 1

while c <= 10:
    print('%i - ' % termo, end='')
    termo += razão
    c += 1
print('\033[1;31mFIM')