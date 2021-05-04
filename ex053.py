print('---- DETECTOR DE PALÍMDROMO ----')

frase = str(input('Digite uma frase qualquer: ')).strip().lower()
frasejunta = frase.split()
frasejunta2 = ''.join(frasejunta[0:])
inverso = ''

for letra in range(len(frasejunta2) - 1, -1, -1):
    inverso += frasejunta2[letra]
print('O inverso de %s é %s' % (frasejunta2, inverso))

if inverso == frasejunta2:
    print('Sim, esta frase é um palíndromo!')
else:
    print('Não, esta frase não é um palíndromo!')
