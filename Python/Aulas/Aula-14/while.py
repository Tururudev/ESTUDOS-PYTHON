#uso de while
#for c in range(1,10):
    #print(c)

#r = "s"
#while r == "s":
    #num = int(input("Digite um valor: "))
    #r = input("Quer continuar [S/N]? ").lower()

#print("FIM") 

n = 1
cont_par = 0
cont_impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1

print("A quantidade de numeros digitados impares e igual a {} e quantidade de numeros digitados pares e igual a {}".format(cont_impar, cont_par))
 