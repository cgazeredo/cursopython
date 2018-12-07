n1 = float(input('Digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1+n2)/2
if media >= 6.0:
    print('Você está aprovado!')
    print('Media é: {:.1f}'.format(media))
else:
    print('Você está reprovado!')
    print('Media é: {:.1f}'.format(media))