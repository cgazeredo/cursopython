valor_casa = float(input('Favor entre com o valor do imóvel: R$ '))
salario = float(input('Favor entrar com o salário no contracheque do comprador: R$ '))
anos_financiamento = int(input('Em quantos anos será feito o financiamento? '))

prestacao = valor_casa/(anos_financiamento*12)
if prestacao >= salario*0.3:
    print('Infelizmente seu financiamento não foi aprovado para {} anos.'.format(anos_financiamento))
    print('A prestação de R${:.2f} excede o limite máximo para sua renda.'.format(prestacao))
else:
    print('Seu financiamento de {} anos foi aprovado.'.format(anos_financiamento))
    print('Sua prestação mensal será de R${:.2f} para um imóvel de R${:.2f}.'.format(prestacao, valor_casa))
