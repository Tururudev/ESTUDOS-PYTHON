total_alunos = 5
soma_idade = 0
aluno_novo = float("inf")
cont = 0
print("Bem-vindo ao sistema de análise de dados de alunos!")
print("---------------------------------------------------")

for i in range(1, total_alunos + 1):
    nome = input(f"Digite o nome do {i} aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    print("---------------------------------------------------")
    
    soma_idade +=  idade

    if (idade < aluno_novo):
        aluno_novo = idade
        nome_novo = nome
    
    if (nota > 7):
        cont += 1

mediaI = soma_idade / total_alunos

print("A media das idades dos alunos e de {:.1f}".format(mediaI))
if aluno_novo:
    print("O aluno mais novo e {}".format(nome_novo))
else:
    print("Nao ha alunos registrados")
if cont > 7:
    print("{} alunos tiraram nota maior que sete".format(cont))
else:
    print("Nao ha alunos com notas maiores que sete!")




    



    