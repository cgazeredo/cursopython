numero = int(input('Entre com um numero inteiro qualquer: '))
base = int(input('Informe a base de conversão desejada: \n1-Binario\n2-Octal\n3-Hexadecimal'))
if base == 1:
    print('O valor convertido de {} em Binario é: {}'.format(numero, numero))
elif base == 2:
