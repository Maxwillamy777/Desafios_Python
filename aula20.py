#def titulo(txt):
 #   print(30 * '-')
  #  print(txt)
   # print(30 * '-')



#titulo('   Curso em Vídeo   ')
#titulo('   Aprenda Python   ')
#titulo('   Gustavo Guanabara   ')
#def soma(a, b):
 #   print(f'A = {a} e b = {b}')
  #  s = a + b
   # print(f'A soma A + B = {s}')


#soma(4, 5)
#soma(8, 9)
#soma(2, 1)
#soma(b=4, a=5)
#soma(2, 3)


#def contador(* num):
    #for valor in num:
     #   print(f'{valor} ', end='')
#print('Fim')
 #   tam = len(num)
  #  print(f'Recebi os valores {num} e são ao todo {tam} números ')

#contador(2, 1, 7)
#contador(8,0)
#contador(4,4,7,6,2)
def dobra(ist):
    pos = 0
    while pos < len(ist):
        ist[pos] *= 2
        pos += 1


valores = [3, 6, 0]
dobra(valores)
print(valores)







