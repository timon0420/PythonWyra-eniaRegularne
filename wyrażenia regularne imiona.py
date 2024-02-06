import re
txt = open('imiona.txt', 'r').read().strip('\n')
lista = []
lista = txt.split('\n')

for i in lista:
    if re.match('.*a$', i):
        print(i, ' To jest kobieta')
    else:
        print(i, ' To nie jest kobieta')