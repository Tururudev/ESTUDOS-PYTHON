dist = float(input("Digite a distancia da viagem: "))
if dist <= 200:
    passag = dist * 0.50
    print("O preco da passagem vai ser de {:.2f}R$".format(passag))
else:
    passag = dist * 0.45
    print("Por ser uma viagem de que passou de 200Km, voce pagar o valor de {:.2f}R$".format(passag))