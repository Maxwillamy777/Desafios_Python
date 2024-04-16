from datetime import datetime
people = {}
people['named'] = str(input('Name: '))
nasc = int(input('Year of birth: '))
people['age'] = datetime.now().year - nasc
people['ctps'] = int(input('Work card(0 does´t have it): '))
if people['ctps'] !=0:
   people['hiring'] = int(input('Year of hiring: '))
   people['Salary'] = int(input('Salary £: '))
   people['retirement'] = (people['age']+((people['hiring'] + 35) - datetime.now().year))
print('-=' * 30)
for k, v in people.items():
    print(f' -{k} have the value {v}')
