nome = input('Qual é o seu nome? ')
print('O nome é {:>20} !'.format(nome))


n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}. A multiplicacao {}. A divisao {:.3f}.'.format(s, m, d), end='\n\n\n\n')
print('A divisao inteira {}. A exponenciaçao {}'.format(di, e))
