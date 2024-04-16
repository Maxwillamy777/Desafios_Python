from ex108 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {(moeda.metade(p, True))} é {moeda.moeda(moeda.metade(p, True))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 10%, temos {moeda.moeda(moeda.aumentar(p, 10, True))}')