#input
x = input('welk codontype? ')

#berekening
if x == 'AUG':
    print('Het codon ' + x + ' is een start codon.')
elif x == 'UAG' or x == 'UGA' or x == 'UAA':
    print('Het codon ' + x + ' is een stop codon.' )
else:
    print('Het codon ' + x + ' is een gewoon codon.')

if x >