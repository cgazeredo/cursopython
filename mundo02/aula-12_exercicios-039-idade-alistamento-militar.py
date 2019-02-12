from datetime import date

ano = int(input('Entre com o ano de nascimento do jovem: '))

idade = date.today().year - ano

if idade > 18:
    print('Você já passou da {} ano(s) da idade de alistamento.'.format(idade-18))
elif idade < 18:
    print('Voce deve se alistar em {} ano(s).'.format(18-idade))
else:
    print('Voce deve se alistar este ano.')
