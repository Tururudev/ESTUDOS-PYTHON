#bases numericas
num = int(input("Digite um numero qualquer: "))
print("""Escolha uma das bases para fazer a conversao: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ]converter para hexadecimal""")
opcao = int(input("Sua opcao: "))
if (opcao == 1):
    print("{} convertido para BINARIO, equivale a {}.".format(num, bin(num)))
if (opcao == 2):
    print("{} convertido para OCTAL, equivale a {}.".format(num, oct(num)))
if (opcao == 3):
    print("{} convertido para HEXADECIMAL, equivale a {}".format(num, hex(num)))
else:
    print("Opcao invalida, tente novamente!")
    
