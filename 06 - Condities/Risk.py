#input
a = float(input('geef getal 1: '))
b = float(input('geef getal 2: '))
c = float(input('geef getal 3: '))
d = float(input('geef getal 4: '))
e = float(input('geef getal 5: '))

# sorteren
f = max(a, b, c,)
g = max(d, e)
h = a + b + c - f - min(a, b, c,)
i = d + e - g

# wie wint
if f > g and h > i:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
elif f <= g and h <= i:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
else:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')