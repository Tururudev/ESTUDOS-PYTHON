num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input("Digite um numero [999 para parar]: "))
    cont += 1
    cont_Final = cont - 1
    soma += num
    soma_final = soma - 999
print("O valor da soma dos {} numeros digitados foi de {}".format(cont_Final, soma_final))
    
