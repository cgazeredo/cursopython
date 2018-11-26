from math import hypot

cateto1 = float(input('Informe o valor do cateto oposto: '))
cateto2 = float(input('Informe o cateto adjacente: '))
hipo = hypot(cateto1, cateto2)

print('O valor da hipotenusa para os catetos {} e {} é {:.2f}. '.format(cateto1, cateto2, hipo))
