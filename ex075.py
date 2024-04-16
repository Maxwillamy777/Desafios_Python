a = int(input(f'Digite 1° valor: '))
b = int(input(f'Digite 2° valor: '))
c = int(input(f'Digite 3° valor: '))
d = int(input(f'Digite 4° valor: '))
tuple = (a,b,c,d)
print(f' The quantity of nine entered:{tuple.count(9)} e a posiçao que parece pela primeira vez o 3:{tuple.index(3) + 1}')
if a % 2 == 0:
    print(f'Número par:{a}')
if b % 2 == 0:
    print(f'Número par:{b}')
if c % 2 == 0:
    print(f'Número par:{c}')
if d % 2 == 0:
    print(f'Número par:{d}')
