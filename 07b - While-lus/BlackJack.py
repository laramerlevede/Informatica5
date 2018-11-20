#uitvoer
kaart = int(input('Welke kaart? '))
totaal = 0

#bewerking
while totaal < 21 and kaart > 0:
    totaal += kaart
    if totaal < 21:
        kaart = int(input('Welke kaart? '))

if kaart == 0:
    antw = 'Voorzichtig gespeeld ({})'.format(totaal)

if totaal == 21:
    antw = 'Gewonnen! '

if totaal > 21:
    antw = 'Verbrand ({})'.format(totaal)

#uitvoer
print(antw)