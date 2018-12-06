nome = input('Digite seu nome: ').strip()
n = nome.split()
print('O seu primeiro nome é {}. '.format(n[0]))
print('Seu último nome é {}. '.format(n[len(n)-1]))
print('Seu último nome é {}. '.format(n[-1]))  # posição -1 é a primeira posiçao da direita pra esquerda EM PYTHON