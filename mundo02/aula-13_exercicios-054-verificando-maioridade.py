# entre com 7 anos de nascimento e diga quantos sao maiores e quantos nao
from datetime import date

# variaveis inicializadas
atual = date.today().year
maioridade = 0
menor = 0
invalido = 0


print('Informe 7 anos de nascimento, para verificação de maioridade')
for c in range(0, 7):
    ano = int(input('Informe o {}º ano: '.format(c+1)))
    if atual - ano >= 21:
        maioridade += 1
    elif atual - ano <= 0:
        invalido += 1
    else:
        menor +=1
print('Temmos {} maiores de idade e {} menores de idade. '.format(maioridade, menor))
if invalido > 0:
    print('Tivemos {} anos digitados que são invalidos e não foram contabilizados. '.format(invalido))
