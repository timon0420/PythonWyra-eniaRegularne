import re

txt = 'bananmangobananjagoda'
wzor = 'banan'
print(re.findall(wzor, txt))
dopasowanie = re.search(wzor, txt)
print(dopasowanie.group())
print(dopasowanie.start())
print(dopasowanie.end())
print(dopasowanie.span())

tekst = re.sub(wzor, r'brzoskwinia', txt)
print(tekst)