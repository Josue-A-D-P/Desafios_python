#Desafio 1038 Lanche:

'''Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade 
deste item. A seguir, calcule e mostre o valor da conta a pagar.
    Codigo/ especificações /  Preço
      1     Cachorro Quente   4.00
      2     XSalada           4.50
      3     Xbacon            5.00
      4     TorradaS          2.00
      5     Refrigerante      1.50



Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de 
um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 
casas após o ponto decimal.

Exemplo de Entrada:
3 2

Exemplo de Saída:
Total: R$ 10.00'''


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