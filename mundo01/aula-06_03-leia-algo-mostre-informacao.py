digite = input('Digite algo: ')
print('O tipo deste dado é:', type(digite))
if digite.isnumeric():
    print('É um numero.')
if digite.isalnum() and not(digite.isnumeric()):
    print('É um alfanumérico.')
if digite.isupper():
    print('Todas são maiusculas.')
else:
    print('Nem todos são maiusculos.')
print(digite.isalpha())