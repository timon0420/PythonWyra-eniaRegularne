import re

if re.match('^[A-Z][a-z]*$', 'Alamakota'):
    print('Dopasowano')
else:
    print('Nie Dopasowano')
# ? oznacza że znak może wystąpić tylko raz 
if re.match('^[A-Z][a-z]?[A-Z]$', 'AlA'):
    print('Dopasowano')
else:
    print('Nie Dopasowano')
# {minimalna ilość wystąpień znaku, maksymalna ilość wystąpień znaku}
if re.match('^[A-Z][a-z]{1,5}$', 'Ania'):
    print('Dopasowano')
else:
    print('Nie Dopasowano')