numero = int(input('Entre com o número para verificar se é primo: '))
if numero <= 1:
    print('Este número não é primo.')
else:
    for c in range(2, numero+1):
        if numero % c == 0 and numero != c:
            print('Este número não é primo.')
            break
        else:
            print('Este número é primo.')
            break

