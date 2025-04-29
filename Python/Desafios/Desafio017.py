#catetos e hipotenusas
co = float(input("Digite a medida do cateto oposto: "))
ca = float(input("Digite a medida do acateto adjacente: "))
hip = ((co ** 2 + ca ** 2) ** (1/2))
print ("A hipotenusa vai medir {}".format(hip))

#com import
from math import hypot
co = float(input("Digite a medida do cateto oposto: "))
ca = float(input("Digite a medida do acateto adjacente: "))
hip = hypot(co, ca)