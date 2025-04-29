lista = []
while True:
    num = int(input("Digite um numero: "))
    lista.append(num)
    continuar = input("Você deseja continuar? [S ou N] ").upper().strip()
   
    while continuar != "S" and continuar != "N":
        continuar = input("Você deseja continuar? [S ou N] ").upper().strip()
    
    if ("N" in continuar):
        print("----------------------------------------")
        print(f"Voce digitou os valores {lista}")
        print(f"Voce digitou {len(lista)} elementos.")
        lista.sort(reverse=True)
        print(f"Os valores em forma decrescente são: {lista}")
        print("O valor 5 faz parte da lista!" if 5 in lista else "O valor 5 não faz parte da lista!")
        break
