n1 = float(input('Digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1+n2)/2
if media >= 7.0:
    print('Você está aprovado!')
    print('Media é: {:.1f}'.format(media))
elif 6.9 >= media >= 5.0:
    print('Você está de recuperação!')
    print('Media é: {:.1f}'.format(media))
else:
    print('Você está reprovado!')
    print('Media é: {:.1f}'.format(media))