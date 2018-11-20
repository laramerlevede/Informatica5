#invoer
woord = str(input('Geef verborgen woord: '))
geld = int(input('Geef gedraaid geldbedrag: '))
letter = str(input('Geef letter: '))
totaal_geld = 0
x = ''

#bewerking
while letter in woord and letter not in x:
    totaal_geld += geld
    x += letter
    letter = str(input('Geef letter: '))

if letter not in woord:
    totaal_geld += 0

#uitvoer
print(totaal_geld)