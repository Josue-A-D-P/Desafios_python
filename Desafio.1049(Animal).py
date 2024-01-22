#Desafio Animal

palavra_1 = str(input())
palavra_2 = str(input())
#palavra_3 = str(input())

vertebrado = {
'ave' : {
    'carnivoro': 'aguia', 
    'onivoro': 'pomba',
        'mamifero' : {
        'onivoro': 'homem', 
        'herbivoro': 'vaca'
        }
    }
}


inseto = {'hematofago': 'pulga', 'herbivoro': 'lagarta'}
anelideo = {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}

invertebrado = inseto, anelideo


if palavra_1 == vertebrado and palavra_2 == ave :
    print(vertebrado['ave'])
    
'''elif palavra_1 == vertebrado and palavra_2 == mamifero:
    print(mamifero) 

elif palavra_1 == invertebrado and palavra_2 == inseto :
    print(inseto)
    
elif palavra_1 == invertebrado and palavra_2 == anelideo :
    print(anelideo) '''
    

