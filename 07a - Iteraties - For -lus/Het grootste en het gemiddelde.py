# input
aantal_getallen = int(input('Aantal getallen: '))
max = 0
som = 0

# berekeningen
for i in range(aantal_getallen):
    getal = int(input('geef getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

gemiddelde = round((som / aantal_getallen), 2)

# output
print('{} {:d} {} {:.2f}' .format('Het grootste getal is', max, 'en het gemiddelde is', gemiddelde))