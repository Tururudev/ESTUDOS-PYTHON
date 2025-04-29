#PA
n1 = int(input("Qual vai ser o primeiro termo da PA? "))
raz = int(input("Qual vai ser a razao da PA? "))
an = n1 + (10 - 1) * raz
for pa in range(n1, an + raz, raz):
    print(pa)