preco = float(input('Qual o preço normal do produto? R$'))
condicao = str(input('A condição de pagamento será à vista ou parcelado? '))

if condicao == 'à vista':
    condicao_vista = str(input('O pagamento será feito em dinheiro cheque ou cartão? '))
    if condicao_vista == 'dinheiro' or condicao_vista == 'cheque':
        preco_final = preco*0.9
    else:
        preco_final = preco * 0.95
else:
    condicao_parcelado = int(input('O pagamento pode ser feito em 2 e 3 vezes. Escolha uma das opçoes: '))
    if condicao_parcelado == 2:
        preco_final = preco
    elif condicao_parcelado == 3:
        preco_final = preco*1.2
    else:
        print('Condição escolhida invalida. ')
print('O preço final do produto para o pagamento escolhido é de R${:.2f}'.format(preco_final))

