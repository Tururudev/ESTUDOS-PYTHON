#maioridade de 7 pessoas
cont = 0
maiorId = 0
menorId = 0
for pess in range(1, 8):
    cont += 1
    nasc = int(input("Digite o seu ano de nascimento da {} pessoa: ".format(cont)))
    idade = 2025 - nasc
    if (idade >= 18):
        maiorId += 1
    else:
        menorId += 1
print("O numero de pessoas com maioridade e de {} pesssoas.".format(maiorId))
print("O numero de pessoas que sao menor de idade e igual a {}".format(menorId))
    


