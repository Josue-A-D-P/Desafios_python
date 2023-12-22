#Desafio calculo Area:

A, B, C =map(float,input().split())

#Calculo de area triângulo retângulo:
Tri_ret = A * C / 2

#Calculo de area circulo :
Circulo = 3.14159 * C ** 2

#Calculo de area trapezio :
Trapezio = (A + B) * C / 2

#Calculo de area Quadrado :
Quadrado = B * B

#Calculo de area Retangulo :
Retangulo = A * B

print(f"TRIANGULO: {Tri_ret:.3f}")
print(f"CIRCULO: {Circulo:.3f}")
print(f"TRAPEZIO: {Trapezio:.3f}")
print(f"QUADRADO: {Quadrado:.3f}")
print(f"RETANGULO: {Retangulo:.3f}")