m = 'M'
n = 'F'
c = 0
while c != m and c != n:
    c = str(input('Informe seu sexo[m/f]:  ')).strip().upper()[0]
    if c != m and c != n:
        print('Tente novamente!')
print('Obrigado!')


