continuar = ""
soma_produtos = 0
produtos_acima_1000 = 0
mais_barato = float("inf")
nome_mais_barato = ""
while True:
    
    print("-------------------------")
    print("   CADASTRANDO PRODUTOS  ")
    print("-------------------------")
    
    nome_produto = input("Qual nome do produto comprado: ")
    
    preco_produto = float(input("Qual preco do produto: R$ "))
    soma_produtos += preco_produto

    if preco_produto > 1000:
        produtos_acima_1000 += 1
    
    if preco_produto < mais_barato:
        mais_barato = preco_produto
        nome_mais_barato = nome_produto
    
    continuar = input("Voce deseja continuar? [S/N] ").upper().strip()
    while (continuar != "S") and (continuar != "N"):
        continuar = input("Voce deseja continuar? [S/N] ").upper().strip()
    
    if (continuar == "N"):
            print("CADASTROS CONCLUIDOS!")
            break
print("------------------------------------------------------------------------------------")
print(f"        A soma total de todos os produtos foi de R$ {soma_produtos:.2f}            ")
print("------------------------------------------------------------------------------------")
if produtos_acima_1000:
    print(f"          {produtos_acima_1000} produtos sao acima de R$ 1000,00 reais             ")
    print("------------------------------------------------------------------------------------")
else:
    print("                Nao ha produtos acima de R$ 1000,00!")
    print("------------------------------------------------------------------------------------")
print(f"      O produto mais barato e o(a) {nome_mais_barato} custando R${mais_barato:.2f}        ")
print("-----------------------------------------------------------------------------------------")
        
       

    

    



    