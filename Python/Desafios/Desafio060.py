#Fatorial

n = int(input("Digite um numero para ser calculado o seu fatorial: "))
c = n
f = 1
while (c > 0):
    print("{}".format(c))
    c -= 1
    f = f * c
print(f)
