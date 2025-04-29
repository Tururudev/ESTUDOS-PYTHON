#senha

from time import sleep

senha = input("Qual senha voce deseja colocar: ")
seg_tentativa = input("Confirme a senha: ") 
cont = 0


while (seg_tentativa != senha):
    cont += 1
    print("--------------------------------------------------------------------------")
    print("                     {} TENTATIVA".format(cont))
    print("--------------------------------------------------------------------------")
    seg_tentativa = input("Voce digitou a senha errado, digite igual da ultima vez: ")
        
    if (cont >= 3):
        cont += 1
        print("--------------------------------------------------------------------------")
        print("                   TENTATIVAS EXCEDIDAS           ")
        sleep(3)
        print("                       ENCERRANDO!                 ")
        print("--------------------------------------------------------------------------")
        break

        
if (seg_tentativa == senha):
    print("Seja bem vindo!")    