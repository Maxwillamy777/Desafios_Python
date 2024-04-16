n = float(input("Quantos quilõmetros o carro alugado percorreu ?:"))
n1 = int(input('Quantos dias o carro alugado passou ?:'))
n2 = n * 0.15
n3 = n1 * 60
n4 = n2 + n3
print("O carro alugado passou  dia: {} ,logo custará R${} \n,agora o quilometros que rodou foram  {} , com taxa fica  R${} \n. No total á pagar R${} ".format(n1, n, n2, n3, n4))