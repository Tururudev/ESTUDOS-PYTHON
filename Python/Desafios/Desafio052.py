num = int(input("Diga um numero inteiro: "))
tot = 0
totI = 0
for c in range(1, num +1):
    if (num % c == 0):
        print("{} DIVISIVEL".format(c))
        tot += 1
    else:
        print("{} N DIVISIVEL".format(c))
        totI += 1
print("O numero {} foi divisivel {}".format(num, tot))
print("O numero {} foi indivisivel {}".format(num, totI))
if (tot == 2):
    print("NUMERO PRIMO")
else:
    print("NUMERO COMPOSTO")
    


