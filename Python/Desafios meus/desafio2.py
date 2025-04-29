total_funcionario = 5
soma_salarios = 0
mais_antigo = 0
nome_mais_antigo = ""
cont_salario = 0
cont_salario_baixo = 0

for i in range(1, total_funcionario + 1):
    print("-----------------------------------")
    print("Funcionario numero {}º".format(i))
    print("-----------------------------------")
    nome = input("Qual seu nome: ")
    tempo = int(input("Qual seu tempo de casa (em anos): "))
    salario = float(input("Qual seu salario (R$): "))
    soma_salarios += salario

    if (tempo > mais_antigo):
        mais_antigo = tempo
        nome_mais_antigo = nome

    if (salario > 5000):
        cont_salario += 1
    else:
        cont_salario_baixo += 1

    media_salarios = soma_salarios / total_funcionario
print("-----------------------------------------------------------------------------------------------")
print("A media salarial total e de R$ {:.2f}".format(media_salarios))
if (nome_mais_antigo):
    print("O funcionario mais antigo e o {} com {} tempo de casa".format(nome_mais_antigo, tempo))
else:
    print("Nao ha alunos registrados!")
if (salario > 5000):
    print("{} funcionarios recebem mais do que R$ 5.000,00 e {} recebem menos que R$ 5.000,00".format(cont_salario, cont_salario_baixo))

    





