# Desafio sort simples
valor_1, valor_2, valor_3 = map(int,  input().split())


lista = [valor_1, valor_2, valor_3]

lista_ordenada = sorted(lista)

for x in lista:
    print(x)

print()

for x in lista_ordenada:
    print(x)