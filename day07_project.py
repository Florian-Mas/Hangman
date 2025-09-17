"""
le jeu commence
faire un mot secret
le cacher
demander une lettre
    si elle est bonne alors afficher toutes les lettre correspondante
    si elle est mauvaise enlever une vie
possibilité de dire un mot
    si c'est le bon, l'afficher
    si c'est le mauvais, enlever une vie
si le mot est trouver félicité 
si le nombre de vie est à 0 faire recommencer et afficher le mot a trouver
recommencer par la suite




"""


import random as rd
from english_words import english_words_lower_set as EWLS






def defeat(try_attempte):
    if try_attempte <= 12:
        print("You loose!")

def random_item():
    liste_random = [1, 2, 3, 4, 5, 6]
    print(rd.choice(liste_random))

#all_word=[]
#for i in EWLS:
#    all_word.append(i)
def choose_a_word():
    
    #print(rd.choice(all_word))
    print(rd.choice(list(EWLS)))

#choose_a_word()


def hidding_word(a_word):
    print("_ "*len(a_word))

#hidding_word("funny")






#début du projet
    #choisi un mot et cache puis renvois dans une liste
def choose_hid_word(a_word):
    #fait une liste ayant des tiret correspondant au nombre de lettre
    hiden_word_secret = ["_"]*len(a_word)
    #renvoie le mot et le mot caché (0 le mot et 1 le mot caché)
    return a_word, hiden_word_secret


    #ce qui permet d'initié le programe
def start():
    #récupère le mot et le mot caché dans start_return (0 le mot et 1 le mot caché)
    hiden_word_real = choose_hid_word(rd.choice(list(EWLS)))
    #print la liste de tiret hors d'une liste grace au *
    print(*hiden_word_real[1])
    #choisi le nombre de vie par défault
    life = 10
    print(f"try to found the word by typing one lettre or the word. You start with {life} life")
    #renvoie le mot et le mot caché (0 le mot et 1 le mot caché) dand le 0 et life dans le 1
    return hiden_word_real, life



    #pour savoir ce que l'utilisateur entre et vérifie si c'est bon 
def ask_lettre_number(hiden_word_real,life,letter_to_guess,letter_already_guessed):
    #le mot cherché visible
    #print(hiden_word_real[0])
    #en cas de perte de toutes la vie, inscrire une défaite
    if life == 0:
        print(f"Tu as perdu, il ne te reste plus de vie. \ntu y arrivera surement la prochaine fois. \nLe mot était {hiden_word_real[0]}\n ")
        return lunch_a_game()
    #demande à l'utilisateur de faire une tentative
    user_guess = input("Make your choise : ")
    #vérifie si c'est une lettre ou un mot
    if len(user_guess) == 1:
        #si la lettre est dans le mot
        if user_guess in letter_to_guess:
            while user_guess in letter_to_guess:
                #mettre a jour la liste qui a les _ pour ajouter les lettre
                hiden_word_real[1].insert(letter_to_guess.index(user_guess),user_guess)
                #supprime le tiret qui est remplacer par la lettre
                hiden_word_real[1].pop(letter_to_guess.index(user_guess)+1)
                #met a jour le mot qui sert de vérification
                letter_to_guess = letter_to_guess.replace(user_guess," ",1)

            #print après la boucle le mot avec les lettre
            print(*hiden_word_real[1])
            #liste de lettre qui sont utilisé
            letter_already_guessed.append(user_guess)
            letter_already_guessed.sort()
            print(f"les lettres qui ne marchent pas/utiliser : {letter_already_guessed}")
            #vérifie si le mot est entièrement dévoilé
            if len(hiden_word_real[0]) == letter_to_guess.count(" "):
                print(f"tu as trouver le mot, c'est : {hiden_word_real[0]}\n")
                return lunch_a_game()
            else:
                #fait une récursive pour réapeler la variable avec les bonne valeur actualisé
                return ask_lettre_number(hiden_word_real,life,letter_to_guess,letter_already_guessed)
        else:
            #en cas de mauvaise tentative, enlever une vie, dire combien il reste de vie puis redemander une lettre
            life -= 1
            print(f"il te reste : {life} life ")
            #lettre qui sont utilisé
            letter_already_guessed.append(user_guess)
            letter_already_guessed.sort()
            print(f"les lettres qui ne marchent pas/utiliser : {letter_already_guessed}")
            return ask_lettre_number(hiden_word_real,life,letter_to_guess,letter_already_guessed)
    else:
        #si c'est une tentative de mot et qu'elle est réussite alors on propose de refaire une parti
        if user_guess == hiden_word_real[0]:
            print(f"bien jouer, le mot rechercher était bien {hiden_word_real[0]}\nsee you next time \n")
            return lunch_a_game()
        
        #evite les mauvaise manipulation de double entré donc de faire un blanc en tentative
        elif user_guess == "":
            print("tu ne peux pas ne pas faire de tentative ")
            return ask_lettre_number(hiden_word_real,life,letter_to_guess,letter_already_guessed)

        #si c'est manqué, enlever une vie puis continué
        else:
            life -= 1
            print("Pas le bon mot, dommage ")
            print(f"il te reste : {life} life")            
            return ask_lettre_number(hiden_word_real,life,letter_to_guess,letter_already_guessed)
    



def lunch_a_game():
    #proposer de faire une partie
    wanted = input ("do you want to do a game ? yes/no ")
    if wanted == "yes":
        #récupère dans start_return le renvoie de start(le mot, le mot caché [0] et life [1])
        start_return = start()
        #récupère dans ask_return les élément nécésaire
        ask_return = ask_lettre_number(start_return[0],start_return[1],start_return[0][0],[])


lunch_a_game()











    