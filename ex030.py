n = float(input('De um número para dize-lo de é par ou impar !:'))
n2 = n // 2
n3 = n2 - n
if n3>=0:
    print('Seu número {} é par !'.format(n))
else:
    print('Seu número {} é impar !'.format(n))
