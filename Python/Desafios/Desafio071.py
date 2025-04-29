print("------------------")
print("  BANCO DO KAUA   ")
print("------------------")
while True:
    valor_saque = int(input("Qual valor voce quer sacar? "))
    while valor_saque <= 0:
        print("---------------------------------------------")
        print("NUMERO INVALIDO. FAVOR DIGITE UM NUMERO POSITIVO")
        print("---------------------------------------------")
        valor_saque = int(input("Qual valor voce quer sacar? "))
        print("---------------------------------------------")

    
    # Inicializa as variáveis para as notas
    quant_notas_50 = quant_notas_20 = quant_notas_10 = quant_notas_1 = 0

    # Calcula a quantidade de notas de R$ 50
    quant_notas_50 = valor_saque // 50

    if valor_saque > quant_notas_50 * 50:  # Se sobrar algum valor após as notas de 50
        valor_faltando = valor_saque - (quant_notas_50 * 50)
        quant_notas_20 = valor_faltando // 20
    
    if valor_saque > (quant_notas_50 * 50) + (quant_notas_20 * 20):  # Se sobrar algum valor após as notas de 20
        valor_faltando = valor_saque - ((quant_notas_50 * 50) + (quant_notas_20 * 20))
        quant_notas_10 = valor_faltando // 10

    if valor_saque > (quant_notas_50 * 50) + (quant_notas_20 * 20) + (quant_notas_10 * 10):  # Se sobrar algum valor após as notas de 10
        valor_faltando = valor_saque - ((quant_notas_50 * 50) + (quant_notas_20 * 20) + (quant_notas_10 * 10))
        quant_notas_1 = valor_faltando // 1

    # Exibe o resultado
    print(f"Voce vai precisar de {quant_notas_50} notas de R$ 50")
    print(f"Voce vai precisar de {quant_notas_20} notas de R$ 20")
    print(f"Voce vai precisar de {quant_notas_10} notas de R$ 10")
    print(f"Voce vai precisar de {quant_notas_1} moedas de R$ 1")

    print("------------------------------------------------------")
    print("    VOLTE SEMPRE AO BANCO DO KAUA ALVES. OTIMO DIA     ")
    print("------------------------------------------------------")
    break