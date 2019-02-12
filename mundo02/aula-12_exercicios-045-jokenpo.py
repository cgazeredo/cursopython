from random import choice
from time import sleep


# Opções do PC
lista = ['pedra', 'papel', 'tesoura']
# Inicializando a opçao do usuario para nao quebrar o while
opcao_user = ''

#prints de inicializacao
print(67*'=')
print('Vamos jogar Jokenpo com o computador!! (para encerrar digite sair)')
print('VAMOS LÁ!')
# este while eh para continuar jogando ate a opçao sair ser ditigada
while opcao_user != 'sair':
    print('\033[;31;mJO')
    sleep(1)
    print('\033[;34;mKEN')
    sleep(1)
    print('\033[1;35;mPO')

    opcao_pc = choice(lista)

    # pegando a opçao do usuario
    opcao_user = str(input('\033[;;mQual sua opção? ')).strip().lower()
    if opcao_user == 'sair':
        print('FIM DE JOGO, ATÉ A PROXIMA!')
        break
    elif opcao_user != 'pedra' and opcao_user != 'papel' and opcao_user != 'tesoura':
        print('OPÇÃO INVALIDA, JOGO ENCERRADO.')
        break

    # considerando as alternativas
    if opcao_user == opcao_pc:
        print('COMPUTANDO...')
        sleep(3)
        print('Voce colocou {} e o Computador {}. '.format(opcao_user, opcao_pc))
        print('EMPATE')
    elif (opcao_user == 'pedra' and opcao_pc == 'tesoura') or (opcao_user == 'papel' and opcao_pc == 'pedra') or (opcao_user == 'tesoura' and opcao_pc == 'papel'):
        print('COMPUTANDO...')
        sleep(3)
        print('Voce colocou {} e o Computador {}. '.format(opcao_user, opcao_pc))
        print('PARABENS VOCÊ GANHOU!')
    else:
        print('COMPUTANDO...')
        sleep(3)
        print('Voce colocou {} e o Computador {}. '.format(opcao_user, opcao_pc))
        print('NÃO FOI DESSA VEZ, O COMPUTADOR TE VENCEU.')




