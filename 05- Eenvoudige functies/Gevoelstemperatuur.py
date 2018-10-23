#input
t = float(input('geef de luchttemperatuur: '))
w = float(input('geef de windsnelheid: '))

#berekening
gevoelstemperatuur = 13.12 + (0.6215 * t) + ((0.3965 * t) - 11.37) * w ** 0.16
print(gevoelstemperatuur)