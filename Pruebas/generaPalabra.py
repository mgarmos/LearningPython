import random


letras = ['Du', 'Du-dei', 'Du', 'Du-dei',' ']

frase = []
# Randomly append 'enemy' or 'friend' or None to the frase list
for n in range(4):
    frase = []
    while len(frase) < 8:
        computer_choice = random.choice(letras)
        frase.append(computer_choice)

    print(frase)