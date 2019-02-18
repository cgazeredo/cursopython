

#  variaveis auxiliares
soma = 0
maior = 0
qtd_20 = 0

for c in range(0, 4):
    print(12*'-', end='')
    print('{}ª PESSOA'.format(c+1), end='')
    print(12*'-')
    nome = str(input('Entre com o nome: '))
    idade = int(input('Entre com a idade: '))
    sexo = str(input('Entre com o Sexo (M/F): '))

    #  guardando a soma das idades:
    soma += idade

    if idade > maior and sexo == 'M':
        maior = idade
        nome_maisvelho = nome
    if idade < 20 and sexo == 'F':
        qtd_20 += 1
media = soma/4

print('A media de idades do grupo é {:.1f}. '.format(media))
print('O nome do homem mais velho é {} e sua idade é {}. '.format(nome_maisvelho, maior))
print('Existe(m) {} mulher(es) com menos de 20 anos.'.format(qtd_20))