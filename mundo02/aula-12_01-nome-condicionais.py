nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que belo nome feminino!')

print('Tenha um bom dia, {}!'.format(nome))
