#input
t = float(input('geef de tijd: '))
c = 299792458
n = 1.000277

#berekening
d = ((c * t) / (2 * n)) * 10**-9

print(str(d) + ' meter')
