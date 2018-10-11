# antwoord op de vragen
hendel_trekken = input('Trek aan de hendel van de wissel? ')
man_duwen = input('Man van brug duwen? ')

# aantal doden berekenen
if hendel_trekken == 'ja' and man_duwen == 'ja':
    print('2')
elif hendel_trekken == 'nee' and man_duwen == 'nee':
    print('5')
else:
    print('1')


