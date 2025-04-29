#IMC
peso = float(input("Digite o seu peso (Kg): "))
alt = float(input("Digite a sua altura (m): "))
imc = peso / (alt **2)
print("Seu IMC e de {:.2f}".format(imc))
if (imc < 18.5):
    print("Voce esta abaixo do peso! Se alimente melhor!")
elif (imc >= 18.5) and (imc <= 25):
    print("Voce esta no peso ideal! Mas nao deixe de se preocupar!")
elif (imc >= 25) and (imc <= 30):
    print("Voce esta com sobrepeso, coma melhor!")
elif (imc >= 30) and (imc <= 40):
    print("Obesidade, isso e preocupante, procure um medico, Rapido!")
else:
    print("OBESIDADE MORBIDA, VOCE VAI MORRER")