número = int(input("Digite um númerode 0 até 9999: "))
u = número // 1 % 10
d = número//10 % 10
c = número//100 % 10
m = (número // 1000 % 10)
print("Unidade: {}".format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
