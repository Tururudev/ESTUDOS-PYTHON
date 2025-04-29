#Seno, cosseno e tangente
import math
ang = float(input("Digite um angulo qualquer: ")) 
seno = math.sin(math.radians(ang))
print("O angulo {} tem o SENO de {:.2f}".format(ang, seno))
cos = math.cos(math.radians(ang))
print("O angulo de {} tem o COSSENO de {:.2f}".format(ang, cos))
tang = math.tan(math.radians(ang))
print("O angulo de {} tem TANGENTE de {:.2f}".format(ang, tang))
  