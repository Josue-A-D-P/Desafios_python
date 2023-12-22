#Desafio O maior:

a, b, c = map(int,input().split())

if a > b:
    result = a
else:
    result = b

if result < c:
    result = c

print(f"{result} eh o maior")
