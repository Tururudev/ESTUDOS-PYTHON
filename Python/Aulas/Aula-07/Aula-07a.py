#Operadores aritméticos
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2 
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma vale {} \no produto vale {}  \na divisao {:.3f}".format(s, m, d))
print("A divisao inteira vale {}  \npotencia vale {}".format(di, e))