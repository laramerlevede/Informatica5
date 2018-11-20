# input
aantal_getallen = int(input('Aantal getallen: '))
max = int(input('geef getal: '))
som = max

# berekeningen
for i in range(aantal_getallen - 1):
    getal = int(input('geef getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

gemiddelde = round((som / aantal_getallen), 2)

# output
print('{} {:d} {} {:.2f}' .format('Het grootste getal is', max, 'en het gemiddelde is', gemiddelde))