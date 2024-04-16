print('-='*20)
print('A existência do triãngulo !')
print('-='*20)
a = float(input('Primeira mediada: '))
b = float(input('A segunda medida: '))
c = float(input('A terceira medida: '))
if a + b  > c and a + c > b:
    print(' Dentro da lei existencial do triãngulo, é possível forma-lo com essas medidas !')
else:
    print('Não é possível forma-lo !')
