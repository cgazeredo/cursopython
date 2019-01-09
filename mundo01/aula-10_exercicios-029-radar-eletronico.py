velocidade = float(input('Qual a velocidade do carro? '))
if velocidade <= 80:
    print('Voce está dentro do limite.')
else:
    print('Você foi multado!')
    print('Valor da multa: {:.2f}'.format((velocidade-80)*7))
