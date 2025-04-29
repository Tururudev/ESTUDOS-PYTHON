soma = cont = 0
while True:
    num = int(input("Digite um numero inteiro [999 para parar]: "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"A soma dos {cont} foi de {soma}")