#radar
velo = float(input("Qual foi a velocidade que o carro passou: "))
if velo > 80:
    print("Voce foi Multado")
    multa = (velo - 80) * 7
    print("E o valor da multa foi {}".format(multa))
else:
    print("Tenha um bom dia e dirija com seguranca")