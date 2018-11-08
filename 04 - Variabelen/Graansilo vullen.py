#input
b = float(input('geef de breedte: '))
l = float(input('geef de lengte: '))
c = float(input('geef kubieke meter per hectare: '))
r = float(input('geef de straal: '))
h = float(input('geef de hoogte: '))
from math import pi

#berekening
inhoud_graansilo = pi * r ** 2 * h
