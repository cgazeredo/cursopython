numero = int(input('Entre com um numero inteiro qualquer: '))
base = int(input('Informe a base de conversão desejada: \n1-Binario\n2-Octal\n3-Hexadecimal\n => '))

print('O valor convertido de {} em'.format(numero), end='')
if base == 1:
    resto = 0
    binario = ''
    while numero >= 2:
        resto = int(numero%2)
        numero = int(numero/2)
        binario = str(resto)+binario
    binario = str(numero)+binario
    print(' Binario é: {}'.format(binario))

if base == 2:
    resto = 0
    octal = ''
    while numero >= 8:
        resto = int(numero % 8)
        numero = int(numero / 8)
        octal = str(resto) + octal
    octal = str(numero) + octal
    print(' Octal é: {}'.format(octal))

if base == 3:
    resto = 0
    hexa = ''
    h_base = ['A', 'B', 'C', 'D', 'E', 'F']
    if  numero >= 16:
        while numero >= 16:
            resto = int(numero % 16)
            if resto > 9:
                resto = h_base[resto-10]
            numero = int(numero / 16)
            hexa = str(resto) + hexa
        hexa = str(numero) + hexa
    else:
        if numero-10 >= 0:
            hexa = h_base[numero - 10]
        else:
            hexa = numero
    print(' Hexa é: {}'.format(hexa))

