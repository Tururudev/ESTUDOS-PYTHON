#alistamento
nasc = int(input("Informe seu ano de nascimento: "))
idade = 2025 - nasc
print("Voce possue {} anos".format(idade))
if (idade < 18):
    alist = 18 - idade
    print("Como voce ainda tem {} anos, voce ainda tera que se alistar!".format(idade))
    print("Voce tera que se alistar daqui a {} anos.".format(alist))
elif (idade == 18):
    print("Como voce ja tem {} anos, esta na hora de se alistar!".format(idade))
else:
    passou = idade - 18
    print("Como voce ja tem {} anos , ja passou {} ano do tempo de se alistar!".format(idade, passou))