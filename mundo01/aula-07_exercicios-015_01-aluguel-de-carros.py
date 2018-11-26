dias = int(input('Quantos dias de aluguel? '))
km_rodados = float(input('Quantos km rodados? '))
valor_aluguel = 60 * dias + 0.15 * km_rodados
print('O total a pagar é de R${:.2f}'.format(valor_aluguel))
