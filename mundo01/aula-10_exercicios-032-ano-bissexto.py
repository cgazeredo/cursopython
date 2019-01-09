from datetime import date

ano = int(input('Qual ano voce quer analisar? Digite 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
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
