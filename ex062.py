print('-=' * 10)
print('Gerador de P.A')
print('-=' * 10)

primeiro = int(input('Informe o primeiro termo (de onde a progressão começará): '))
razão = int(input('Informe a razão: '))
termo = primeiro
c = 1
total = 0
mais = 10


while mais != 0:
    total += mais
    while c <= total:
        print('%i - ' % termo, end='')
        termo += razão
        c += 1
    print('\033[1;31mPausa...\033[m')
    mais = int(input('Deseja ver mais quantos termos?: '))
print('Progressão finalizada com %i termos' % total)
