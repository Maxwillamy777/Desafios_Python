soma = 0
n = 1
f = 0
d = 0
print('-' * 30)
print('A loja do Max')
print('-' * 30)
while True:
    product = str(input('Whats is name of the product? '))
    price = float(input('Whats is price the R$:'))
    esc = str(input('Continue: yes or no?  ')).upper()
    soma += price
    d = price
    if esc == 'NO':
        break
    if price >= 1000:
        f += n
    elif d < price:
          product = product and d < price
print(f'Total spent on purchase R$: {soma}')
print(f'Number of products that cost equal to or more than 1000 are {f} product(s)')
print(f'Name of the cheapest product: {product}')
print('Closed account!')









