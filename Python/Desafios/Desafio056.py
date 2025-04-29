somaI = 0
Mvelho = 0
idadeM = 0
cont = 0
for dados in range(1,5):
    print("{} PESSOA".format(dados))
    nome = input("Qual seu nome? ")
    nasc = int(input("Quando voce nasceu? "))
    idade = 2025 - nasc
    somaI = somaI + idade
    print("Voce tem {} anos".format(idade))
    print("""Qual seu sexo?  
    [ 1 ] MASCULINO
    [ 2 ] FEMININO""")
    sexo = int(input("Sua escolha: "))
    print("------------------------------------------------")
    if sexo == 1: 
        if idade > Mvelho:
            Mvelho = idade
            Hvelho = nome
    else:
        if idade < 20:
            cont += 1

            
            
        

        
if idade < 20:
    print("Sao {} mulheres abaixo de 20 anos".format(cont))
else:
    print("Não há mulheres no grupo.")

if Hvelho:
    print("O homem mais velho é {} com {} anos.".format(Hvelho, Mvelho))
else:
    print("Não há homens no grupo.")
mediaI = somaI / dados
print("O total das idades foi {} anos".format(somaI))
print("A media de idades e de {} anos".format(mediaI))



    
    
