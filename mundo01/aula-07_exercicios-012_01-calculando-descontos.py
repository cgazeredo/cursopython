p = float(input('Qual é o preço do produto? R$'))
desc = p * 0.05
novo_p = p - desc
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, novo_p))
