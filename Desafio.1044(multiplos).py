#Desafio Multiplos

A, B = map(int, input().split())
cont = 0
result = False

while cont <= 11 and result == False :
    result = A * cont
    cont += 1
    if result == B:
        result = True
    else:
        result = False

if result == True:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")
    