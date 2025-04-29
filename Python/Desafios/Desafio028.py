#jogo de adivinhar
from random import randint
from time import sleep
computador = randint(0,5)
print("Vou pensar em um numero de 0 a 5. Tente adivinhar!")
jogador = int(input("Em que numero eu pensei? "))
print("PROCESSANDO....")
sleep(3)
if jogador == computador:
    print("Voce conseguiu adivinhar o numero que eu pensei, VOCE GANHOU!")
else:
    print("o numero que eu pensei foi {}, VOCE PERDEU!".format(computador))
