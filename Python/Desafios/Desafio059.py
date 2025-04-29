#menu interativo
import time

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite um valor: "))
escolha_usuario = 0

while escolha_usuario != 5:
    time.sleep(1)
    print("O QUE DESEJA FAZER? ")
    print("""    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA""")
    escolha_usuario = int(input("Qual sua escolha? "))

    if (escolha_usuario == 1):
        soma = n1 + n2
        print("-------------------------------------------------")
        print("{} + {} e igual a {}".format(n1, n2, soma))
        print("-------------------------------------------------")
        time.sleep(2)
    elif (escolha_usuario == 2):
        produto = n1 * n2
        print("-------------------------------------------------")
        print("{} x {} e igual a {}".format(n1, n2, produto))
        print("-------------------------------------------------")
        time.sleep(2)
    elif (escolha_usuario == 3):
        if (n1 > n2):
            print("-------------------------------------------------")
            print("{} e maior que {}".format(n1 ,n2))
            print("-------------------------------------------------")
            time.sleep(2)
        elif (n1 == n2):
            print("-------------------------------------------------")
            print("{} e igual a {}".format(n1, n2))
            print("-------------------------------------------------")
            time.sleep(2)
        else:
            print("-------------------------------------------------")
            print("{} e maior que {}".format(n2, n1))
            print("-------------------------------------------------")
            time.sleep(2)
    elif (escolha_usuario == 4):
        n1 = float(input("Digite um novo valor: "))
        n2 = float(input("Digite um outro novo valor: "))
        time.sleep(2)
    elif (escolha_usuario != 5):
        print("-------------------------------------------------")
        print("          ESCOLHA UM NUMERO VALIDO"               )
        print("-------------------------------------------------")

print("ENCERRANDO PROGRAMA...")       
time.sleep(2)           
print("ATE LOGO!")

        