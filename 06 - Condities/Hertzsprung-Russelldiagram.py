#input
x = float(input('geef de temperatuur (in Kelvin): '))
y = float(input('geef de lichtkracht: '))

#berekening
if y < 0.01 and x > 5000:
    print('witte dwergen')
elif y < 0.0001 and x > 3000:
    print('witte dwergen')
elif 10 < y < 100 and x < 6000:
    print('reuzen')
elif 100 < y < 1000 and x < 7500:
    print('heldere reuzen')
elif 1000 < y < 10000:
    print('superreuzen (b)')
elif 10000 < y:
    print('superreuzen (a)')
else:
    print('hoofdreeks')