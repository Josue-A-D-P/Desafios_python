#Desafio 1051 imposto de renda:

'''Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em 
seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a 
tabela abaixo.
            Renda                           /   Imposto de Renda
            de 0.00 a R$ 2000.00                Isento
            de R$ 2000.01 até R$ 3000.00        8%
            de R$ 3000.01 até R$ 4500.00        18%
            acima de R$ 4500.00                 28%

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, 
pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No 
exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que 
resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com 
duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa 
a mensagem "Isento".

Exemplos de Entrada:
3002.00

Exemplos de Saída:
R$ 80.36'''


salario = float(input())

imposto_1 = 0
imposto_2 = 0
imposto_3 = 0

if salario > 0.00 and salario <= 2000.00:
    print('Isento')
else:
    if salario > 4500.00:
        imposto_3 = (salario - 4500.00) * 28 / 100
        cont = salario - 4500.00
        salario = salario - cont
        imposto_2 = (salario - 3000.00) * 18 / 100
        cont = salario - 3000.00
        salario = salario - cont
        imposto_1 = (salario - 2000.00) * 8 / 100
    
    elif salario > 3000.00 and salario < 4500.00:
        imposto_2 = (salario - 3000.00) * 18 / 100
        cont = salario - 3000.00
        salario = salario - cont
        imposto_1 = (salario - 2000.00) * 8 / 100

    else:
        salario > 2000.00 and salario < 3000.00
        salario = salario - 3000.00
        imposto_1 = (salario - 2000.00) * 8 / 100

    tot_imposto = imposto_1 + imposto_2 + imposto_3

    print(f"R$ {tot_imposto:.2f}")