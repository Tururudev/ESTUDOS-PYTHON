#jokenpo
import random
itens = ["PEDRA" , "PAPEL" , "TESOURA"]
computador = random.randint(0, 2)
escoU = (input("Faca sua escolha(PEDRA, PAPEL OU TESOURA) ")).strip().upper()   
if (escoU not in itens):
    print("ESCOLHA INCORRETA, POR FAVOR ESCOLHA ENTRE PEDRA, PAPEL OU TESOURA")
else:
    print("Voce escolheu {} e o computador {}".format(escoU, itens[computador]))

    #VERFIFICACAO DE VITORIA DERROTA OU EMPATE
if (escoU == itens[computador]):
    print("DEU EMPATE!")
    #TODAS CONDICOES DE VITORIA DO USUARIO
elif(escoU == "PEDRA" and itens[computador] == "TESOURA") or \
    (escoU == "PAPEL" and itens[computador] == "PEDRA") or \
    (escoU == "TESOURA" and itens[computador] == "PAPEL"):
    print("VOCE GANHOU")
else:
    print("VOCE PERDEU")
        
    


