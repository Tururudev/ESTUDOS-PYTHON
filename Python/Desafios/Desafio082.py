lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)

    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    
    continuar = input("Deseja continuar? [S/N] ").upper().strip()

    while continuar != "S" and continuar != "N":
        continuar = input("Deseja continuar? [S/N] ").upper().strip()

    if (continuar == "N"):
        print(f"A lista completa é {lista}")
        print(f"A lista dos pares é igual a {lista_par}")
        print(f"A lista dos Ímpares é {lista_impar}")
        break
    

