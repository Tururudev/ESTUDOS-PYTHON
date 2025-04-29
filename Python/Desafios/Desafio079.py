lista = []
while True:
    n = int(input("Digite um numero: "))
    print("NUMERO ADICIONADO COM SUCESSO")
    if n in lista:
        print("NUMERO JA DIGITADO")
        print("DIGITE UM NUMERO QUE NAO FOI DIGITADO AINDA")
    else:
        lista.append(n)
    
    coninuar = input("Quer continuar [S ou N] ").upper().strip()
    if coninuar == "N":
        lista.sort()
        print(lista)
        break
    
    
    
    
    