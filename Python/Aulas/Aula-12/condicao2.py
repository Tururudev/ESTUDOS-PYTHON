#condicoes aninhadas
nome = input("Qual seu nome? ")
if (nome == "gustavo"):
    print("Nome bonito")
elif (nome == "pedro") or (nome == "maria") or (nome == "junior"):
    print("Voce tambem tem um nome comum")
elif nome in ("ana claudia jessica juliana"):
    print("Belo nome feminino")
else:
    print("Seu nome e bem normal")
print("Tenha um bom dia!")