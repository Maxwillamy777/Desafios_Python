from ex108 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {(moeda.moeda(p,))} é {(moeda.metade(p,'sim'))}')
print(f'O dobro de {moeda.moeda(p)} é R${(moeda.dobro(p))}')
print(f'Aumentado 10%, temos {(moeda.aumentar(p, 10,'sim' ))}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13,'sim' )}')