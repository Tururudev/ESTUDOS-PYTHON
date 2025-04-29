#for
i = int(input("Digite o incio: "))
f = int(input("Digite o final: "))
pula = int(input("Digite de quanto em quanto vai pular: "))
s = 0
for c in range(i, f+1, pula):
    print(c)
    s = s + c
print(s)

    