#Acerte o numero
import random


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.randint(0, 9)
num_usuario = int(input("Tente adivinhar qual numero eu escolhi? [1 a 10] "))
cont_tentativa = 0
    
if (num_usuario == escolhido):
    print("Voce acertou o numero escolhido")
    print("Eu escolhi {} e voce escolheu {}".format(escolhido, num_usuario))
    print("------------------------------------------------")

else:
    
    while (num_usuario != escolhido):
        if escolhido > num_usuario:
            print("-------------------------------------------------")
            print("            CHUTE MAIS ALTO                      ")
        elif num_usuario > escolhido:
            print("               MAIS BAIXO"                        )
        
        cont_tentativa += 1
        print("------------------------------------------------")
        print("               VOCE ERROU!                        ")
        print("------------------------------------------------")
        num_usuario = int(input("Tente adivinhar novamente qual numero eu escolhi novamente! [1 a 10] "))

print("------------------------------------------------")
print("                  VOCE ACERTOU!              ")
print("E levou {} tentativas para acertar o numero {}".format(cont_tentativa,escolhido))
print("------------------------------------------------")
    


