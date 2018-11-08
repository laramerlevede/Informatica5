# input
x = int(input('geef getal (<100): '))
som_veelvouden = 0

# overloop
for i in range(x, 101, x):
    som_veelvouden += i

# output
print(som_veelvouden)