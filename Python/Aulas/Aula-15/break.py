n = s = 0
while True:
    n = int(input("Digite um numero: "))
    
    if n == 999:
        break
    
    s += n
#print("A soma dos nuemeros valor {}".format(s))
print(f"A soma vale {s}")
        