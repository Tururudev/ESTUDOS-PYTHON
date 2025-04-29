nome = input("Digite o seu nome completo: ")
dividido = (nome.split())
print("Seu primeiro nome e: ",dividido[0])
print("Seu ultimo nome e: {}".format(dividido[len(dividido)-1]))