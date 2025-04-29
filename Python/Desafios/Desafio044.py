#Descontos
prod = float(input("Qual o valor do produto que vc comprou? R$ "))
print("----------------------------------------------------------")
print("""Escolha o metodo de pagamento
\n[ 1 ] (DINHEIRO OU CHEQUE)
[ 2 ] (A VISTA NO CARTAO)
[ 3 ] (2x NO CARTAO)     
[ 4 ] (3x OU MAIS NO CARTAO)""")
esco = int(input("Sua escolha: "))
print("----------------------------------------------------------")
if (esco == 1):
    desc = prod * (90/100)
    print("Ao escolher a vista no dinheiro, voce recebeu 10% DE DESCONTO")
    print("O valor do prduto era de R$ {:.2f}, passou a ser R$ {:.2f}, apos o desconto".format(prod, desc))
    print("----------------------------------------------------------")
elif (esco == 2):
    desc = prod * (95 / 100)
    print("Ao escolher a vista no cartao, voce recebeu 5% DE DESCONTO")
    print("O valor do prduto era de R$ {:.2f}, passou a ser R$ {:.2f}, apos o desconto".format(prod, desc))
    print("----------------------------------------------------------")
elif (esco == 3):
    print("Voce pagara o preco normal de R$ {:.2f}".format(prod))
    print("----------------------------------------------------------")
elif (esco == 4):
    precoJ = prod * (120 / 100)
    parc = int(input("Quantas parcelas? "))
    parcJ = precoJ / parc
    print("Sua compra sera PARCELADA em {}x de R$ {:.2f}. COM JUROS DE 20%".format(parc, parcJ))
    print("Sua compra que era de R$ {:.2f}, vai custar R$ {:.2f}".format(prod, precoJ))
    print("----------------------------------------------------------")
    
    
    
             