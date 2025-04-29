#comparando numeros
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
if (n1 > n2):
    print("O {} e maior que {}.".format(n1, n2))
elif (n2 > n1):
    print("O {} e maior que {}.".format(n2, n1))
elif (n1 == n2):
    print("{} e {} sao iguais".format(n2, n1))