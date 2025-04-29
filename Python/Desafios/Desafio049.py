#Tabuada de algum numero
num = int(input("Digite um numero para saber sua tabuada: "))
cont = 0 # cont comeca com 0
for tab in range(0, 10, 1):
    cont = cont + 1 #a cada loop o cont vai recebendo +1 que vai ser mutiplicado pelo num escolhido
    calc = num * cont
    print("{} x {} = {}".format(num, cont, calc))
    