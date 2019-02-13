#  entre com 6 numeros e some somente os pares
from time import sleep
soma = 0
print('Digite 6 números e mostrarei a soma de todos os que são pares.')
sleep(1)
for c in range(0, 6):
    numero = int(input('Entre com o {}º numero: '.format(c+1)))
    if numero % 2 == 0:
        soma += numero
if soma != 0:
    print('A soma dos números inseridos que são pares é: {}'.format(soma))
else:
    print('Nenhum numero par foi digitado. ')
