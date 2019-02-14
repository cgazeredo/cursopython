

#variaveis auxiliares
maior = 0
menor = 0



for c in range(0, 5):
    peso = float(input('Digite o peso a ser comparado: '))
    if peso > maior:
        if menor == 0:
            menor = maior
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso digitado foi: {} e o menor foi: {}'.format(maior, menor))
