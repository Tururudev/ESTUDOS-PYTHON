#Empréstimo
print("----------------------------------------------------------------------")
casa = float(input("Digite qual vai ser o preço da casa que você irá comprar: R$"))
sala = float(input("Quanto que voce recebe de salario? R$"))
anos = int(input("Quantos anos voce deseja pagar essa casa? "))
print("----------------------------------------------------------------------")
mens = anos * 12
precMen = casa / mens
if (precMen > (sala * (30/100))):
    print("Para pegar um casa de R${:.2f}, em {} anos, a prestacao sera de R${:.2f}".format(casa, anos, precMen))
    print("Emprestimo negado, voce excedeu 30% do seu salario!")
    print("----------------------------------------------------------------------")
elif (precMen < (sala * (30/100))):
    print("Seu emprestimo foi aceito!")
    print("E tera a parcela de R${:.2f} em {} anos.".format(precMen, anos))
    print("----------------------------------------------------------------------")