#media notas
n1 = float(input("Quanto tirou na primeira prova? "))
n2 = float(input("Qunato tirou na segunda prova? "))
media = (n1 + n2) / 2
if (media < 5):
    print("O aluno foi reprovado, media era 5 e o aluno tirou {}".format(media))
elif (media >= 5) and (media <= 6.9):
    print("O aluno devia tirar mais que 6.9 para nao ficar de recuperacao e tirou {}".format(media))
else:
    print("O aluno foi aprovado! tirou {}, media superior a 7.".format(media))