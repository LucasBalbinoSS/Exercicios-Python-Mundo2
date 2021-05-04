n1 = int(input('Informe o primeiro termo (de onde começará): '))
n2 = int(input('Informe a razão da progressão: '))
dec = n1 + (10 - 1) * n2

for c in range(n1, dec + n2, n2):
    print(c)
