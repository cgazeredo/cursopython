#  Leia o primeiro termo e a razao e calule os 10 primeiros termos de uma PA

a1 = int(input('Entre com o primeiro termo da PA: '))
r = int(input('Entre com a razão da PA: '))

print('Para o primeiro termo {} e razao {}, '.format(a1, r))
print('Os 10 primeiros termos desta PA são: ', end='')
for c in range(a1, a1+9):
    print('{}, '.format(a1), end='')
    a1 += r
print('{}'.format(a1))