import random
escolhido = random.randint(1, 10)
cont_vitorias = 0


while True:
    num = int(input("Escolha um numero: "))
    Par_impar = input("Par ou impar? [I/P]: ").upper().strip()
    while Par_impar not in "PI":
        Par_impar = input("Par ou impar? [I/P]: ").upper().strip()
    
    total = num + escolhido
    print("---------------------------------------------------------------------")
    print(f"Voce escolheu {num} e eu escolhi {escolhido}. Total foi de {total}")
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    print("---------------------------------------------------------------------")
    
    if (total % 2 == 0) and ("P" in Par_impar) or (total % 2 != 0) and ("I" in Par_impar):
        cont_vitorias += 1
        print("VOCE GANHOU")
        print("VAMOS JOGAR NOVAMENTE")
    else:
        print("                     VOCE PERDEU                                ")
        print("----------------------------------------------------------------")
        print(f"GAME OVER! VOCE GANHOU {cont_vitorias}")
        break

        

