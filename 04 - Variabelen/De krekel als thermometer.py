#input
x = float(input('aantal waargenomen tjirps per minuut: '))

#berekening
tf = 50 + (x - 40)/4
tc = 10 + (x - 40)/7

print('temperatuur (Fahrenheit): ' + str(tf))
print('temperatuur (Celsius): ' + str(tc))