import re
# r'tekst' oznacza surowy tekst, (tekst) oznacza to grupę, ?P<nazwa grupy>, ?: oznacza grupę anonimową, | oznacza lub
wynik = re.match(r'^(?P<przywitanie>Hello)( World)+(!|.)$', r'Hello World World!')

if wynik:
    print('Dopasowano')
    print(wynik.group('przywitanie'))
    print(wynik.group(2))
    print(wynik.groups())
else:
    print('Nie dopasowano')
