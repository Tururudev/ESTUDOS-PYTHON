#Pode ou nao triangulo
r1 = float(input("Primeiro segmento: "))
r2 = float(input("segundo segmento: "))
r3 = float(input("terceiro segmento: "))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("Os segmentos podem formar um triangulo")
else:
    print("Os segmentos nao podem formar um triangulo")