lista = []
posicoes_maior = []
posicoes_menor = []
for c in range(0, 5):
    lista.append(int(input(f"Digite o {c + 1}° valor: ")))

maior = max(lista)
menor = min(lista)

posicao_maior = lista.index(maior)
posicao_menor = lista.index(menor)

for i in range(len(lista)):
    if lista[i] == maior:
        posicoes_maior.append(i)
    
    elif lista[i] == menor:
        posicoes_menor.append(i)

print(f"Voce digitou os valores {lista}")

if len(posicoes_maior) > 1:
    print(f"O maior valor digitado foi o {maior} nas posicoes {posicoes_maior}")
else:
    print(f"O maior valor digitado foi o {maior} na posicao {posicao_maior}")

if len(posicoes_maior) > 1:
    print(f"O menor valor digitado foi o {menor} nas posicoes {posicoes_maior}")
else:
    print(f"O menor valor digitado foi o {menor} na posicao {posicao_menor}")





        


