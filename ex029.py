n = float(input('Qual é a velocidade do carro em  km/h ?:  '))
n2 = (n - 80) * 7
if n>80:
    print('O carro foi multado e cobrará de multa R${} !'.format(n2))
else :
    print('O carro não está multado !')
