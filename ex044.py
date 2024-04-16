e = float(input('O valor do produto R$:  '))
print('1-À vista dinheiro/cheque:10% de desconto')
print('2-À vista no cartão:5% de desconto')
print('3-Em até 2x no cartão:preço formal')
print('4-3x ou mais no cartão:20% de juros')
es = int(input('Agora digite o número do pagamento que escolher: '))
if es == 1:
    r = e - (e * 10 / 100)
    print('O preço ficará R${}!'.format(r))
elif es == 2:
    j =(e * 5 / 100) - e
    print('O preço ficará R${}!'.format(j))
elif es ==3:
    f = e / 2
    print('O preço ficará R${}!'.format(f))
elif es == 4:
    d = (e * 20 / 100) + e
    print('O preço ficará R${}!'.format(d))



