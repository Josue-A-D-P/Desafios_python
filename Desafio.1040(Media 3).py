# Desafio Media 3

N1, N2, N3, N4 = map(float, input().split())

Valor_notas = (N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)

Valor_peso = 2 + 3 + 4 + 1

media = Valor_notas / Valor_peso

if media >= 7.0:
    print(f"Media: {media}")
    print("Aluno aprovado.")

elif media < 5.0:
    print(f"Media: {media}")
    print("Aluno reprovado.")
    
else:
    media >= 5.0 and media < 7.0
    print("Aluno em exame.")

    Nota_exame = float(input())

    print(f"Nota do exame: {Nota_exame}")

    result = (media + Nota_exame) / 2

    if result >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {result:.1f}")
    
    else:
        result < 5.0
        print("Aluno reprovado.")
        print(f"Media final: {result:.1f}")