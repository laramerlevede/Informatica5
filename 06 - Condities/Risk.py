#input
a = float(input('geef getal 1 aanvaller: '))
b = float(input('geef getal 2: '))
c = float(input('geef getal 3: '))
d = float(input('geef getal 4: '))
e = float(input('geef getal 5: '))

#wie wint?
f = max(a, b, c,)
g = max(d, e)
h = a + b + c - f - min(a, b, c,)
i = d + e - g
if f > g and h > i:
    x = 0
    y = 2
    print('aanvaller verliest ' + str(x) + ' legers, verdediger verliest ' + str(y) + ' legers')
elif f <= g and h <= i:
    x = 2
    y = 0
    print('aanvaller verliest ' + str(x) + ' legers, verdediger verliest ' + str(y) + ' legers')
elif f <= g and h> i or f > g and h <= i:
    x = 1
    y = 1
    print('aanvaller verliest ' + str(x) + ' leger, verdediger verliest ' + str(y) + ' leger')