def aumentar(n, taxa, b):
    res = n + (n * taxa/100)
    return res


def diminuir(n, taxa, b):
    res = n - (n * taxa/100)
    return res


def dobro(n):
    n *= 2
    return n


def metade(n, b):
    n /= 2
    return n

def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:>2f}'.replace('.',',')

