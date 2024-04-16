import random
n = int(input("Escolha de  um número de 1 á 5 e adivinhe que  número a maquina vai escolher !:  "))
n2: int = random.randint(1, 5)
n3: float = (n - n2)
if n3 == 0:
     print('Você venceu á maquina!:{} '.format(n2))
else:
     print('A maquina venceu!: {} '.format(n2))
