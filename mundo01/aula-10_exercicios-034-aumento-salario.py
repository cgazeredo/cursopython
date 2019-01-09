salario = float(input('Entre com o salario do funcionario: '))

if salario > 1250.00:
    print('Seu novo salário é: R${:.2f}'.format(salario + salario*0.1))
else:
    print('Seu novo salário é: R${:.2f}'.format(salario + salario*0.15))
