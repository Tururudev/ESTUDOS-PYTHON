#PA
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro
cont = 1
continuar = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print("{} - ".format(termo), end=(""))
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quanto stermos voce que rmostrar a mais? "))
print("Progessao finalizada com {} termos".format(total))