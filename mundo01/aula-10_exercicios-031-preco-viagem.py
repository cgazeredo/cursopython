distancia = float(input('Digite a distancia da viagem: '))
if distancia <= 200:
    print('O custo da viagem de {} é : R${:.2f}'.format(distancia, distancia*0.50))
else:
    print('O custo da viagem de {} é : R${:.2f}'.format(distancia, distancia*0.45))
