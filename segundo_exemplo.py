"""
ADIVINHE O NUMERO SECRETO
"""

import random

numero_secreto = random.randint(1,20)
adivinhou = False

while True:
    palpite =(input("Adivinhe o numero (entre 1 e 20):"))
    if palpite == numero_secreto:
        print("Parabens, voce acertou!")
        break
    else:
        print("tente novamente!")