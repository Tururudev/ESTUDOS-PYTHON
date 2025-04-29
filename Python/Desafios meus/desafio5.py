lista = []
lista_multi = []

while True:
    num = int(input("Digite um numero: "))
    lista.append(num)
    

    if num < 0:
        lista.pop()
        print(f"Lista dos numeros: {lista}")
        print("-----------------------------------------------------------------------")
        print("    Escolha o que deseja fazer com a lista dos numeros digitados       ")
        print("-----------------------------------------------------------------------")
        print(""" Escolha uma das opções
              [1] MUTIPLICAR NUMEROS DA LISTA
              [2] DIVIDIR NUMEROS DA LISTA
              [3] SOMAR NUMEROS DA LISTA
              [4] SUBTRAIR NUMEROS DA LISTA""")
        escolha = int(input("Qual sua escolha? "))
        
        while escolha not in {1, 2, 3, 4}:
            print(""" Escolha uma das opções
              [1] MUTIPLICAR NUMEROS DA LISTA
              [2] DIVIDIR NUMEROS DA LISTA
              [3] SOMAR NUMEROS DA LISTA
              [4] SUBTRAIR NUMEROS DA LISTA""")
            escolha = int(input("Escolha um dos numeros acima? "))

        if escolha == 1:
            num_multiplicado = int(input("Qual numero voce deseja mutiplicar a lista: "))
            for c in lista:
                multi = c * num_multiplicado
                lista_multi.append(multi)
            print(f"Lista original: {lista}")
            print(f"Lista com os numeros multiplicados por {num_multiplicado}: {lista_multi}")
            break

    
            
