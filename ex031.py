n = float(input('Qual é a distãncia da viagem?: '))
if n>=200:
    n2 = n * 0.45
    print('Viagem longa , o preço da passagem é R${:.2f}'.format(n2))
else:
    n3 = n * 0.50
    print('O preço da passagem cobrado é R${:.2f}'.format(n3))