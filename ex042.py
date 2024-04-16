print('-=' * 20)
print('A existência do triãngulo !')
print('-=' * 20)
a = float(input('A Primeira mediada: '))
b = float(input('A segunda medida: '))
c = float(input('A terceira medida: '))
d = a + b + c
if a + b > c and a + c > b:
    print(' Dentro da lei existencial do triãngulo, é possível forma-lo com essas medidas !')
if not a + b > c and a + c > b:
    print('Não é possível forma-lo !')
elif d == d // 3 * 3:
    print('Será formado um equilátero.')
elif  b == a  or  c == a or b == c:
    print('Será formado um isósceles.')
else:
    print('Será formado um escaleno.')

