from datetime import date

ano = int(input('Entre com o ano de nascimento do atleta: '))

idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('A categoria do atleta é mirim.')
elif 9 < idade <= 14:
    print('A categoria do atleta é infantil.')
elif 14 < idade <= 19:
    print('A categoria do atleta é junior.')
elif 19 < idade <= 20:
    print('A categoria do atleta é senior.')
else:
    print('A categoria do atleta é master.')





'''
9 mirim
14 infantil
19 junior
20 Senior
acima master
'''