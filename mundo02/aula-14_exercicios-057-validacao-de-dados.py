#Faça um programa que leia o sexo de uma pessoa mas so pode aceitar M ou F

sexo = str(input('Digite o sexo da pessoa:  '))
while sexo != 'M' and sexo != 'F':
    print('Sexo invalido digite novamente')
    sexo = str(input('qual o sexo da pessoa? '))

print('O Sexo é {}'.format(sexo))

