#input
dv = float(input('geef dichtheid vrachtwagens: '))
vv = int(input('geef snelheid vrachtwagens: '))
da = float(input('geef dichtheid personenwagens: '))
va = int(input('snelheid personenwagens: '))

#berekeningen
pv = ((vv * dv), 1)
pa = ((va * da), 1)

if abs(pv - pa) > 0.7:
    mes = 'geel'
elif max(pv) > 0.7 or max(pa) and abs(pv - pa) < 0.2:
    mes = 'rood'
if min(pv) > 0.7 or min(pa) > 0.7:
    mes = 'zwart'
else:
    mes = 'groen'

#uitvoer
print(mes)