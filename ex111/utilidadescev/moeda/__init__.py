def aumentar(n, taxa):
    res = n + (n * taxa/100)
    return res


def diminuir(n, taxa):
    res = n - (n * taxa/100)
    return res


def dobro(n):
    n *= 2
    return n


def metade(n, ):
    n /= 2
    return n

def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:>2f}'.replace('.',',')

def resumo(n):
    print(40 * '-')
    print('           Resumo do valor:')
    print(40 * '-')
    print(f'preço analisado:         R${n}')
    print(f'Dobro do preço:          R${dobro(n)}')
    print(f'Metade do preço:         R${metade(n)}')
    print(f'20% de aumento:          R${aumentar(n,20)}')
    print(f'12% de redução:          R${diminuir(n,12)}')
    print(40 * '-')
