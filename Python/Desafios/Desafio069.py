idade_maior_18 = 0
sexo_masculino = 0
mulher_menor_20 = 0
while True:
    
    print("---------------------")
    print(" CADASTRE UMA PESSOA")
    print("---------------------")
    idade = int(input("Qual a sua idade? "))
    if idade > 18:
        idade_maior_18 += 1
    
    sexo = input("Qual seu sexo? [M/F] ").upper().strip()
    while sexo not in "MF":
        sexo = input("Qual seu sexo? [M/F] ").upper().strip()

    if (sexo in "M"):
        sexo_masculino += 1
    
    if (sexo in "F"):
        if idade < 20:
            mulher_menor_20 += 1
    
    continuar = input("Voce deseja continuar? [S/N] ").upper().strip()
    while continuar not in "SN":
        continuar = input("Voce deseja continuar? [S/N] ").upper().strip()

    if (continuar == "N"):
        print("--------------------------------------------------------------")
        print(f"{idade_maior_18} pessoas tem mais de 18 anos!")
        print(f"{sexo_masculino} pessoas do sexo masculino foram cadastradas!")
        print(f"{mulher_menor_20} mulheres tem a idade menor que 20!")
        print("--------------------------------------------------------------")
        break

    

    




    


    
