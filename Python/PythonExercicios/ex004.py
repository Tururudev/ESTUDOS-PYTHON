#Dissecando uma variavel
a = input("Digite qualquer coisa: ")
print("So tem espacos?", a.isspace())
print("E um numero?", a.isnumeric())
print("E alfabetico?", a.isalpha())
print("E alfanumerico?", a.isalnum())
print("Estao maiuscula?", a.isupper())
print("Estao em minusculas?", a.islower)
print("Esta capitalizado?", a.istitle())
