num1 = int(input('Entre com um numero inteiro qualquer: '))
num2 = int(input('Entre com o segundo numero inteiro qualquer: '))

if num1 > num2:
    print('O numero {} é maior que o numero {}.'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior que o numero {}.'.format(num2, num1))
else:
    print('Os numeros são iguais.')


