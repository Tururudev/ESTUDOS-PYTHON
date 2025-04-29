continuar_program = 0
soma = 0
contar_num = 0
maior_num = 0
menor_num = float("inf")


while continuar_program != "N":
    
    num = int(input("Digite qualquer numero: "))
    print("------------------------------")
    continuar_program = input("Deseja continuar? [S/N] ").upper().strip()
    print("------------------------------")
    
    contar_num += 1
    soma += num
    media_soma = soma / contar_num
    
    if num < menor_num:
        menor_num = num
    
    elif num >= maior_num:
        maior_num = num

print("O maior numero lido foi o {}".format(maior_num))
print("------------------------------")
print("O menor numero lido foi o {}".format(menor_num))
print("------------------------------")
print("A media dos numeros foi {}".format(media_soma))
print("------------------------------")


