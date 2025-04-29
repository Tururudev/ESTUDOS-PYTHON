larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))
area = larg * alt
tinta = area / 2
print("O numero necessario de latas de tinta vai ser {} para pintar uma area de {}".format(tinta, area))