import re
txt = 'Hello World World '
wynik = re.match(r'^Hello(?P<świat> World)+.{1,2}$', txt)

if wynik:
    print('Dopasowano')
    print(wynik.group('świat'))
    zmienna = wynik.group('świat')
    print(len(zmienna)-1)
else:
    print('Nie Dopasowano')
