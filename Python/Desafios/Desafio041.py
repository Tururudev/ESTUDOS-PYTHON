#categoria
nasc = int(input("Em que ano voce nasceu? "))
idade = 2025 - nasc
if (idade <= 9):
    print("Voce tem {} anos.".format(idade))
    print("Voce se adegua na cateoria MIRIM")
elif (idade > 9) and (idade <= 14):
    print("Voce tem {} anos.".format(idade))
    print("Voce se adequea na categoria INFANTIL")
elif (idade > 14) and (idade <= 19):
    print("Voce tem {} anos.".format(idade))
    print("Voce se adequa na categoria JUNIOR")
elif (idade > 19) and (idade <= 20):
    print("Voce tem {} anos.".format(idade))
    print("Voce se adequa na categoria SENIOR")
else:
    print("Voce tem {} anos.".format(idade))
    print("Voce se adequa na categoria MASTER")