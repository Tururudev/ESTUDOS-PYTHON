#soma de 6 numeros inteiros pares
s = 0
cont = 0
for rep in range(1,7):
    cont += 1
    num = int(input("Digite o {} numero: ".format(cont)))
    if (num % 2 == 0):
        s += num
print("A soma dos nuemeros PARES E igual a {}".format(s))
