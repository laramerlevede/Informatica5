# waarden vragen voor x en y
x = float(input('Geef waarde voor x: '))
y = float(input('Geef waarde voor y: '))

#formules
linkerlid = abs(abs(x) - abs(y))
rechterlid = abs(x - y)

#uitvoer
print('{:.4f} ≤ {:.4f}'.format(linkerlid, rechterlid))