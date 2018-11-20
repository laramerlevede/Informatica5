# input
prijs = 1
som = 0

# berekeningen
while prijs > 0:
    prijs = float(input('geef prijs: '))
    som += prijs

#uitvoer
print('De totale prijs is €', '{:.2f}'.format(som))