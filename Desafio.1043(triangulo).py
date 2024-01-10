#Desafio triângulo

A, B, C = map(float, input().split())


if (B - C) < A < (B + C) and (A - C) < B < (A + C) and (A - B) < C < (A + B):
    perimetro_tri = A + B + C
    print(f"Perimetro = {perimetro_tri:.1f}")

else:
    area_trap = (A + B)  * C / 2
    print(f"Area = {area_trap:.1f}")