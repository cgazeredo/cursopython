n = int(input('Digite um numero para ver sua tabuada: '))
print('-'*12)
for c in range(0, 11):
    print('{:2} x {} = {:2} '.format(c, n, n*c))
print('-'*12)


