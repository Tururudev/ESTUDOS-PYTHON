while True:
    print("--------------------------------------------------------")
    num = int(input("Digite um numero para ver a sua tabuada: "))
    print("--------------------------------------------------------")
    
    if num < 0:
        print("SAINDO DO PROGRAMA...")
        break

    for cont in range(1, 10):
        multiplicacao = num * cont
        print(f"{num} x {cont} = {multiplicacao}")


    
    

    
    

