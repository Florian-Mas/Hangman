import random as rd
import os
import sys
import datetime

#print(str(rd.choice(list(my_dictionnary_word))))


#début du projet
"""
def list_of_word():
    list_of_word_good = []
    my_dictionnary_word = open(sys.argv[1],"r")
    for word in my_dictionnary_word:
        count = 0
        word_without_backslash = []
        word_str_without_backslash = ""
        for do_separate in word:
            if len(word)-1 > count:
                word_without_backslash.append(do_separate)
                count += 1
            else:
                count = 0
                for i in word_without_backslash:
                    word_str_without_backslash = word_str_without_backslash + i
                list_of_word_good.append(word_str_without_backslash)
                word_without_backslash.clear()
    return rd.choice(list_of_word_good)
        
"""
def list_of_word():
    with open(sys.argv[1], encoding="utf-8") as my_dictionnary_word :
        words = [line.strip() for line in my_dictionnary_word]
    return rd.choice(words)

    #choisi un mot et cache puis renvois dans une liste
def choose_hid_word(a_word):
    #print(a_word)
    #fait une liste ayant des tiret correspondant au nombre de lettre
    hiden_word_secret = ["_"]*(len(a_word))
    #renvoie le mot et le mot caché (0 le mot et 1 le mot caché)
    return a_word, hiden_word_secret


    #ce qui permet d'initié le programe
def start():
    #récupère le mot et le mot caché dans start_return (0 le mot et 1 le mot caché)
    hiden_word_real = choose_hid_word(list_of_word())
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
        return life
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
                #return lunch_a_game()
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
            #return lunch_a_game()
        
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
    
    return life
    

def ending_the_game(word,life):
    #cherche la date jour/mois/anné/heure/min
    actual_date = datetime.datetime.now()
    actual_date_day = actual_date.strftime("%d")
    actual_date_month = actual_date.strftime("%m")
    actual_date_year = actual_date.strftime("%Y")
    actual_date_hour = actual_date.strftime("%H")
    actual_date_minutes = actual_date.strftime("%M")
    actual_date = str(actual_date_day) +"/"+ str(actual_date_month) +"/"+ str(actual_date_year) +" "+ str(actual_date_hour) +"-"+ str(actual_date_minutes)
    #vérification de la présence de high_score.txt et en cas de non présence, le crée
    if os.path.isfile(os.getcwd()+"/high_score.txt") == False:
        open("high_score.txt","x")
        
    #crée un dictionnaire pour récupérer toutes les infos
    dictionnary_high_score ={}
    #ouvre le fichier ayant les hight_score
    with open(os.getcwd()+"/"+"high_score.txt") as high_score_reminder:
        #faire en sorte de l'adapté pour que ce soit {nom : {date : valeur, tentative : valeur }}
        for line in high_score_reminder: 
            stock = line.split(":")
            stock[1] = stock[1].replace("(","") 
            stock[1] = stock[1].replace(")","")
            stock[1] = stock[1].strip()
            stock[1] = stock[1].split(",")

            dictionnary_high_score[stock[0]] = dict(date = stock[1][0], tentative = int(stock[1][1]))
    #vérifie si le mot est dans le dictionnaire et si c'est le cas alors vérifier que le nombre de tentative enregistrer soit plus grand que ceux fait actuellement
    if word in dictionnary_high_score:
        if dictionnary_high_score[word]["tentative"] > 10 - life:
            new_record = True
            dictionnary_high_score[word]["tentative"] = 10 - life
            #applique le changement de date
            dictionnary_high_score[word]["date"] = actual_date
        else:
            new_record = False
        #pour réenregistrer dans le fichier de high_score
        new_file_to_keep = ""
        #réécrit le fichier high_score sur le programme en tant que string
        for élément in dictionnary_high_score:
            new_file_to_keep += élément + ":(" + dictionnary_high_score[élément]["date"] +"," + str(dictionnary_high_score[élément]["tentative"])+")\n"
        #réécrit le fichier hight_score réelement avec les bon élément grace à la string
        with open(os.getcwd()+"/"+"high_score.txt","w") as high_score_reminder:
            high_score_reminder.write(new_file_to_keep)
        
        
    #si il n'est pas déja présent, l'ajouter à la fin avec la bonne date et le paramettre
    else: 
        with open(os.getcwd()+"/"+"high_score.txt","a") as high_score_reminder:
            high_score_reminder.write(word + ":(" + actual_date + "," + str(10-life)+")\n")
            new_record = True
            
    
    if new_record:
        print(f"Nouveau record battu pour {word}!!!! tu l'as fait en ayant perdu {10-life} vie\n")
    else:
        print(f"Le record actuel est de {dictionnary_high_score[word]["tentative"]} vie perdu. Tu auras plus de chance de le battre la prchaine fois\n")
        
    
    







def lunch_a_game():   
    #récupère dans start_return le renvoie de start(le mot, le mot caché [0] et life [1])
    start_return = start()
    #récupère dans ask_return les élément nécésaire
    ask_return = ask_lettre_number(start_return[0],start_return[1],start_return[0][0],[])
    if ask_return > 0:
        ETG = ending_the_game(start_return[0][0],ask_return)
        
       
    




try:
    open(os.getcwd()+"/name_for_hangman.txt")
except:
    print("pas de base de donnée faite, merci de remplir les donné dans un fichier name_for_hangman.txt")
else:
    try:
        sys.argv[1]
    except:
        print("     Il manque l'argument pour avoir la liste de mot.\n \n  Écrire : python3 day09_project.py name_for_hangman.txt\n\n (name_for_hangman peut etre remplacé par n'importe quel fichier txt qui possède un mot par ligne qui devra etre deviné)")
        playing = False
    else:
        playing = True




        


    while playing:
        #proposer de faire une partie
        wanted = input ("do you want to do a game ? yes/no ")
        if wanted == "yes":
            all_stat_in_game = lunch_a_game()

        else:
            playing = False

