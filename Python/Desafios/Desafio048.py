#Soma de impares que sao multiplos de 3 de 1 a 500
s = 0
cont = 0
for num in range(1, 501, 1):
    if (num % 2 != 0) and (num % 3 ==0):
        cont = cont + 1
        s = s + num
        print(num)
print("A soma de todos os {} foi de {}".format(cont, s))
        
