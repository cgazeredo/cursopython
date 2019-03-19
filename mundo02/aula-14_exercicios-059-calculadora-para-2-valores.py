v1 = float(input('Digite o valor 1: '))
v2 = float(input('Digite o valor 2: '))


print('Opções:')
print(' [1] Somar')
print(' [2] Multiplicar')
print(' [3] maior')
print(' [4] novos numeros')
print(' [5] sair')

opcao = int(input('Digite sua opção: '))

while opcao != 5:
    if opcao == 1:
        print('{} + {} = {} '.format(v1, v2, v1+v2))
        print('')
    elif opcao == 2:
        print('{} x {} = {}'.format(v1, v2, v1*v2))
        print('')
    elif opcao == 3:
        if v1>v2:
            print('Entre {} e {} o maior é: {} '.format(v1, v2, v1))
            print('')
        elif v2>v1:
            print('Entre {} e {} o maior é: {} '.format(v1, v2, v2))
            print('')
        else:
            print('Os numeros são iguais.')
            print('')
    elif opcao == 4:
        print('Entre com os novos numeros:')
        v1 = float(input('Digite o novo valor 1: '))
        v2 = float(input('Digite o novo valor 2: '))
    elif opcao == 5:
        print('CABÔ! ^_^')
        print('')
        break
    else:
        print('Opção inválida, tente novamente')


    print('Opções:')
    print(' [1] Somar')
    print(' [2] Multiplicar')
    print(' [3] maior')
    print(' [4] novos numeros')
    print(' [5] sair')

    opcao = int(input('Digite sua opção: '))

print('CABÔ! ^_^')
print('')

