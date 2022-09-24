#this is a very stupid little game that I've made yesterday
import random

#my first ever project
n = random.randint(1, 10)
print('Sto pensando ad un numero tra 1 e 10...')

# pretty dumb I know
running = True
while running:
    numero_indovinato = input('Prova ad indovinare')
    indovino = int(numero_indovinato)

    if indovino == n:
        print('Bravo, come hai fatto ad indovinare...')
        
        running = False

    elif 0 < indovino < n:
        print('No, mi spiace, troppo piccolo :(')

    elif indovino < 1:
        print('Ho detto da 1 a 10, non meno di 1! >:(')

    elif indovino > 10:
        print('Ho detto da 1 a 10, non più di 10! >:(')

    elif n < indovino <= 10:
        print('No, mi spiace, troppo grande :(')
