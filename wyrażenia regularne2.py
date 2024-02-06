import re


# '.' zastępuje każdy znak '.*' zastępuje dowolną ilość znaków '^' oznacza od czego musi zaczynać się wzór '$' oznacza na czym musi kończyć się wzór [Kk] klasa znaków [A-Z] przedział znaków
#if re.match('^[A-Z].t$', 'Kot'):
#    print('Dopasowano')
#else:
#    print('Nie dopasowano')

if re.match('^[Rr]ok[-=][0-9][0-9][0-9][0-9]', 'rok-2022'):
    print('Dopwsowano')
else:
    print('Nie dopasowano')