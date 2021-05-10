n1 = int(input('Informe o primeiro termo (de onde a progressão começará): '))
n2 = int(input('Informe a razão: '))
c = 0

while c < 10:
    print(n1)
    c += 1
    n1 += n2
print('\033[1;31mFIM')