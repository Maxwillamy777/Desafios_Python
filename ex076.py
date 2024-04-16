
a = 'Pizza', 12.50,'Ambuguer',13,'Torta',14,'Bucho',18,'Salada',6,'Pastel',12.50,'Coca-cola',5,'Pepsi',7,'Traviola',8.50,'Batata-Frita',10
print(40 * '-')
print('Cárdapio:')
print(40 * '-')
o = 20 * '.'
for p in range(0, len(a)):
    if p % 2 == 0:
       print(f"{a[p]:.<30}",end='')
    else:
        print(f"R${a[p]:>7.2f}")
print(40 * '-')