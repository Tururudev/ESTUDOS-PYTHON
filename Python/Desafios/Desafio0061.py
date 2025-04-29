#PA
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro
cont = 1
continuar = 0
while cont <= 10:
    print("{} - ".format(termo), end=(""))
    termo += razao
    cont += 1
print("FIM")
mais = int(input("Quanto stermos voce que rmostrar a mais? "))


