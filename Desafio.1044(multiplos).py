#Desafio Multiplos

def sao_multiplos(A, B):
    if A % B == 0 or B % A == 0:
        return "Sao Multiplos"
    else:
        return "Nao sao Multiplos"

A, B = map(int, input().split())


resultado = sao_multiplos(A, B)
print(resultado)