#Desafio tipos de triangulo

def classificar_triangulo(a, b, c):
    lados = sorted([a, b, c], reverse=True)
    a, b, c = lados

    
    if a >= b + c:
        print("NAO FORMA TRIANGULO")
        return

    
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")

    
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")


a, b, c = map(float, input().split())

classificar_triangulo(a, b, c)

