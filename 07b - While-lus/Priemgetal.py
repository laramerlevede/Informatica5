#input
getal = int(input('Geef het getal: '))
n = 2
i = 1

#berekening
while n < getal:
    if (getal % n) == 0:
        antw = '{} is geen priemgetal'.format(getal)
        i = 0
    n += 1
if i and getal != 1:
    antw = '{} is een priemgetal'.format(getal)
elif getal == 1:
    antw = '1 is geen priemgetal'

#uitvoer
print(antw)