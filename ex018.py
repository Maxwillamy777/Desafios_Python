import math
ãngulo = float(input('Digite o ãngulo que você deseja: '))
seno = math.sin(math.radians(ãngulo))
print('O ãngulo de {} tem o seno de {:.2f}'.format(ãngulo, seno))
cosseno = math.cos(math.radians(ãngulo))
print('O ãngulo de {} tem o cosseno de {:.2f}'.format(ãngulo,cosseno))
tangente = math.tan(math.radians(ãngulo))
print('O ãngulo de {} tem a tangente de {:.2f}'.format(ãngulo, tangente))


