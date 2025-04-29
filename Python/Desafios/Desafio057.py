sexo = input("Informe seu sexo [M/F] ").upper().strip()

while sexo != "M" and sexo != "F":
    print("Dados invalidos. Por favor, informe seu sexo [M/F]")
    sexo = input("Informe seu sexo [M/F]: ").upper().strip()

print("SEXO CADASTRADO")
