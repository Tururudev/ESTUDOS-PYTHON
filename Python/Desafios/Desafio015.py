#Aluguel de carros
dist = float(input("Qual quantidade de quilometros(Km) foi percorrida? "))
dias = int(input("Quantos o carro foi alugado? "))
preco = ((60 * dias) + (0.15 * dist))
print("O total preco total para alugar o carro em {} dias e {}Km percorridos e de {}".format(dias, dist, preco))