ano = int(input('Digite um ano: '))

if ano%4 == 0:
    if ano%100 == 0:
        if ano % 400 == 0:
            print('Ano {} é Bissexto.'.format(ano))
        else:
            print('Ano {} não é bissexto.'.format(ano))
    else:
        print('Ano {} é Bissexto.'.format(ano))
else:
    print('Ano {} não é bissexto.'.format(ano))
