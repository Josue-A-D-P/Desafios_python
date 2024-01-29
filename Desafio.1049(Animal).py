#Desafio 1049 Animal:

'''Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

Exemplos de Entrada:
vertebrado
mamifero
onivoro

Exemplos de Saída:
homem'''


palavra1 = input()
palavra2 = input()
palavra3 = input()


if palavra1 == 'vertebrado':
    if palavra2 == 'ave':
        if palavra3 == 'carnivoro':
            resultado = 'aguia'
        elif palavra3 == 'onivoro':
            resultado = 'pomba'
    elif palavra2 == 'mamifero':
        if palavra3 == 'onivoro':
            resultado = 'homem'
        elif palavra3 == 'herbivoro':
            resultado = 'vaca'
elif palavra1 == 'invertebrado':
    if palavra2 == 'inseto':
        if palavra3 == 'hematofago':
            resultado = 'pulga'
        elif palavra3 == 'herbivoro':
            resultado = 'lagarta'
    elif palavra2 == 'anelideo':
        if palavra3 == 'hematofago':
            resultado = 'sanguessuga'
        elif palavra3 == 'onivoro':
            resultado = 'minhoca'

print(resultado)