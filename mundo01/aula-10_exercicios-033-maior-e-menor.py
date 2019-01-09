n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
n3 = int(input('Digite o numero 3: '))

if n1 <= n2:
    if n1 <= n3:
        print('O menor é {}'.format(n1))
    else:
        print('O menor é {}'.format(n3))
elif n2 <= n3:
    print('O menor é {}'.format(n2))
else:
    print('O menor é {}'.format(n3))

if n1 >= n2:
    if n1 >= n3:
        print('O maior é {}'.format(n1))
    else:
        print('O maior é {}'.format(n3))
elif n2 >= n3:
    print('O maior é {}'.format(n2))
else:
    print('O maior é {}'.format(n3))


