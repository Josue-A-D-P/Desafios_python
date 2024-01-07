#Desafio Fórmula de Bhaskara:

A, B, C = map(float, input().split())

try:
    delta = (B**2) - 4 * A * C

    x = delta ** (1/2)

    r1 = ((- B) + x) / (2 * A)  
    r2 = ((- B) - x) /(2 * A)   


    print(f"{r1:.5f}")
    print(f"{r2:.5f}")
except:
    print("Impossivel calcular")