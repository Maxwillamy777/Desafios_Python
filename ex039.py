#idade = int(input('Quantos anos vc tem ?: '))
#if idade == 18:
    #print('Em sua idade , voce já deve de alistar !')
#elif idade > 18:
   # a = idade - 18
  #  print('Já passou {} ano(s) para o seu alistamento '.format(a))
#else:
   # a = 18 - idade
   # print('Ainda você vai de alistar daqui á {} ano(s)'.format(a))
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Vc tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Aida faltam {} anos para o alistamento'.format(saldo))

elif idade  > 18:
    saldo = idade - 18
    print('Vc já deveria ter se alistado há {} anos.'.format(saldo))