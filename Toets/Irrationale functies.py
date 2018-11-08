#input
a = float(input('geef x (een reël getal): '))
from math import sqrt as vierkantswortel

#berekeningen
if a == 2:
    mes = '{:.2f} {}'.format(a, ' is nulpunt van f')
elif a > 2:
    b = vierkantswortel(a - 2)
    mes = '{}{:.2f}{}{:.2f}'.format('f(',a,') = ',b)
else:
    mes = '{:.2f}{}'.format(a, ' ∉ dom(f)')

#uitvoer
print(mes)