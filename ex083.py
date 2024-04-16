list = list()
print(25 * '=-')
print('EXPRESSIONS ANALIYZER!')
print(25 * '=-')
while True:
 expression = (input('ENTER AN EXPRESSION: '))
 if (expression.count('(')) - (expression.count(')')) == 0:
  print('YOUR EXPRESSION IS VALID!')
  list.append(expression)
 else:
  print('THE EXPRESSION IS INCORRECT!')
 answer = (input(str('WANT CONTINUE [Y/N]? '))).lower()
 if answer[0] == 'n':
  print('PROGRAM CLOSED!')
  break
print(25 * '=-')
print(f'YOUR LIST IS EXPRESSIONS VALID:{list}')
print(25 * '=-')
