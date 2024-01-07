#Desafio Lanche

codigo, quantidade = map(int, input().split())

Cachorro = 4.00
XSalada = 4.50
Xbacon = 5.00
TorradaS = 2.00
Refrigerante = 1.50


if codigo == 1:
    total = Cachorro * quantidade

elif codigo == 2:
    total = XSalada * quantidade

elif codigo == 3:
    total = Xbacon * quantidade

elif codigo == 4:
    total = TorradaS * quantidade

else:
    codigo == 5
    total = Refrigerante * quantidade

print(f"Total: R$ {total :.2f}")