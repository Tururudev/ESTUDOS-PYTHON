#palindromo
frase = str(input("Digite uma palavra para verificarmos se e um palindromo: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    print(junto[letra])
