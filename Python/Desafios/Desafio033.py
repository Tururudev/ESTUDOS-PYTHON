#Maior e menor numero
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
if (n1 > n2) and (n1 > n3):
    print("O maior numero e o {}".format(n1))
elif (n2 > n1) and (n2 > n3):
    print("O maior numero e o {}".format(n2))
elif (n3 > n1) and (n3 > n2):
    print("O maior numero e o {}".format(n3))
if (n1 < n2) and (n1 < n3):
    print("O menor numero e o {}".format(n1))
elif (n2 <n1) and (n2 < n3):
    print("O menor numero e o {}".format(n2))
elif (n3 < n1) and (n3 < n2):
    print("O menor numero e o {}".format(n3))

    