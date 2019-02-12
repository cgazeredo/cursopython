peso = float(input('Entre com o peso da pessoa: '))
altura = float(input('Entre com a altura em metros da pessoa: '))


imc = peso / (altura**2)

if imc < 18.5:
    print('Voce esta abaixo do peso. Seu IMC é {:.2f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Voce esta no peso ideal. Seu IMC é {:.2f}'.format(imc))
elif 25 <= imc < 30:
    print('Voce esta com sobrepeso Seu IMC é {:.2f}'.format(imc))
elif 30 <= imc < 40:
    print('Voce esta na faixa de obesidade. Seu IMC é {:.2f}'.format(imc))
else:
    print('Voce esta na faixa de obesidade morbida. Seu IMC é {:.2f}'.format(imc))

