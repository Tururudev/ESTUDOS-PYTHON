#Aumento salario
sal = float(input("Digite o valor do seu salario: "))
if (sal > 1250):
    aum = sal * (110 / 100)
    print("Seu novo salario sera no valor de {:.2f}R$".format(aum))
elif (sal <= 1250):
    aum = sal * (115 / 100)
    print("Seu novo salario sera de {:.2f}R$".format(aum))

