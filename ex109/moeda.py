def aumentar(n=0, taxa=0, b='não'):
    res = n + (n * taxa/100)
    return res if not b else moeda(n)


def diminuir(n=0, taxa=0, b ='não'):
    res = n - (n * taxa/100)
    return res if not b else moeda(n)


def dobro(n=0, b='não'):
    res = n * 2
    return n if not b  else moeda(res)


def metade(n=0, b='não'):
     res = n / 2
     # noinspection PyTypeChecker
     return res if not b  else moeda(res)

def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:>2f}'.replace('.',',')

