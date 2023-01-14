import matplotlib.pyplot as plt
import csv
import pickle
import numpy as n
import json
import itertools
import time

n.random.seed(0)
def TriCocktail(liste):
    echange=True
    while echange==True :
        echange=False
        for i in range (0,len(liste)-2):
            if liste[i]>liste[i+1] :
                tmp=liste[i]
                liste[i]=liste[i+1]
                liste[i+1]=tmp
                echange=True
        for i in range(len(liste)-2,0,-1):
            if liste[i] > liste[i + 1]:
                tmp = liste[i]
                liste[i] = liste[i + 1]
                liste[i + 1] = tmp
    return liste

def Tri_Insertion(l):
    for i in range(1,len(l)):
        x=l[i]
        j=i
        while j>0 and l[j-1]>x :
            l[j]=l[j-1]
            j=j-1
        l[j]=x

    return l

def TriFusion(L):
    if len(L) == 1:
        return L
    else:
        return fusion(TriFusion(L[:len(L) // 2]), TriFusion(L[len(L) // 2:]))


def fusion(A, B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] <= B[0]:
        return [A[0]] + fusion(A[1:], B)
    else:
        return [B[0]] + fusion(A, B[1:])


def rechercheDichotomique(tab,x):
    debut=0
    fin=len(tab)-1
    while debut <= fin :
        milieu=(debut+fin) //2
        if tab[milieu]==x :
            return milieu
        elif tab[milieu] > x:
            fin =milieu-1
        else :
            debut=milieu+1
    return "element non trouve"


def recherche_dichotomique_recursive(liste, element_rechercher, debut, fin):
    if debut > fin:
        return "Élément non trouvé"

    milieu = (debut + fin) // 2

    if liste[milieu] == element_rechercher:
        return milieu

    elif liste[milieu] > element_rechercher:
        return recherche_dichotomique_recursive(liste, element_rechercher, debut, milieu - 1)

    else:
        return recherche_dichotomique_recursive(liste, element_rechercher, milieu + 1, fin)


def TirageLoto():

    data = n.random.choice(range(1,46),5, replace=False)


    return data


def sauvegarde_csv(x):
    with open('sauvegarde-1.csv', 'w', newline='') as f:
        writer = csv.writer(f,delimiter=';')

        for i in range(0, x):
            tirage = TirageLoto()
            print(tirage)
            # Écrit la ligne dans le fichier CSV en utilisant writerows()
            writer.writerows([tirage])


def sauvegarde_json(x):


    # Crée une liste vide pour stocker les lignes de nombres

    rest_dct={}
    for i in range(0, x):
        rest_dct[f"Tirage numero {i+1} "]=TirageLoto().tolist()
        #print(rest_dct[f"Tirage numero {i+1} "])

    print(rest_dct)
    # Ouvre un fichier en écriture
    with open('sauvegarde-2.json', 'w') as f:
        # Écrit chaque ligne au format JSON dans le fichier
        json.dump(rest_dct, f)




def chargement_json(fichier):
    try:
        with open(fichier, 'r') as f:
            donnees = json.load(f)

            return donnees
    except Exception as e:
        print(e)

def chargement_csv(fichier):
    try:
        listeTransformer=[]
        with open(fichier, 'r') as f:
            donnees = csv.reader(f,delimiter=";")

            for ligne in donnees :
                for i in range(0, len(ligne)):
                    ligne[i] = int(ligne[i])
                listeTransformer.append(ligne)
        return listeTransformer
    except Exception as e:
        print(e)



def Chargemement_Sauvegarde_Tri_csv(a,x):
    listee = []
    match a:
        case "TriCocktail":
            for i in range(0, x):
                charg = chargement_csv('sauvegarde-1.csv')[i]
                print(f"Tirage triee numero {i + 1} " + str(TriCocktail(charg)))
                listee.append(charg)
            with open('sauvegarde-1.csv', 'w', newline='') as f:
                for l in listee:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerows([l])
            print("la liste Triee a bien était sauvegarder dans le fichier sauvegarde-1.csv\n")
        case"TriInsertion":
            for i in range(0, x):
                charg = chargement_csv('sauvegarde-1.csv')[i]
                print(f"Tirage triee numero {i + 1} " + str(Tri_Insertion(charg)))
                listee.append(charg)
            with open('sauvegarde-1.csv', 'w', newline='') as f:
                for l in listee:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerows([l])
            print("la liste Triee a bien était sauvegarder dans le fichier sauvegarde-1.csv\n")
        case "TriFusion":
            for i in range(0, x):
                charg = chargement_csv('sauvegarde-1.csv')[i]
                t = TriFusion(charg)
                print(f"Tirage triee numero {i + 1} " + str(t))
                listee.append(t)
            with open('sauvegarde-1.csv', 'w', newline='') as f:
                for l in listee:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerows([l])
            print("la liste Triee a bien était sauvegarder dans le fichier sauvegarde-1.csv\n")

def ChargementListTriee_RechercheD_csv(rech_d):
    if rech_d == "RechercheDichotomique":
        b = int(input("Quel nombre voulez vous connaitre sa position ?"))
        for i in range(0, x):
            charg = chargement_csv('sauvegarde-1.csv')[i]
            if type(rechercheDichotomique(charg, b)) == int:
                print(
                    f"le nombre {b} de la liste numero {i + 1} : se trouvant a la place numero {rechercheDichotomique(charg, b) + 1}")
            else:
                print(rechercheDichotomique(charg, b))
    elif rech_d == "RechercheDichotomiqueRecursive":
        b = int(input("Quel nombre voulez vous connaitre sa position ?"))
        for i in range(0, x):
            charg = chargement_csv('sauvegarde-1.csv')[i]
            if type(recherche_dichotomique_recursive(charg, b, 0, len(charg))) == int:
                print(
                    f"le nombre {b} de la liste numero {i + 1} : se trouvant a la place numero {recherche_dichotomique_recursive(charg, b, 0, len(charg)) + 1}")
            else:
                print(recherche_dichotomique_recursive(charg, b, 0, len(charg)))


def Chargemement_Sauvegarde_Tri_json(a,x):
    dictio = {}
    listee = []
    match a:
        case "TriCocktail":
            for i in range(0, x):
                listee = TriCocktail(chargement_json('sauvegarde-2.json')[f"Tirage numero {i + 1} "])
                dictio[f"Tirage numero {i + 1} "] = listee
                print(f"Tirage triee numero {i + 1} " + str(listee))
            with open('sauvegarde-2.json', 'w') as f:
                # Écrit chaque ligne au format JSON dans le fichier
                json.dump(dictio, f)
                print("la liste Triee a bien était sauvegarder dans le fichier sauvegarde-2.json\n")
        case "TriInsertion":
            for i in range(0, x):
                listee = Tri_Insertion(chargement_json('sauvegarde-2.json')[f"Tirage numero {i + 1} "])
                dictio[f"Tirage numero {i + 1} "] = listee
                print(f"Tirage triee numero {i + 1} " + str(listee))
            with open('sauvegarde-2.json', 'w') as f:
                # Écrit chaque ligne au format JSON dans le fichier
                json.dump(dictio, f)
                print("la liste Triee a bien était sauvegarder dans le fichier sauvegarde-2.json\n")
        case "TriFusion":
            for i in range(0, x):
                listee = TriFusion(chargement_json('sauvegarde-2.json')[f"Tirage numero {i + 1} "])
                dictio[f"Tirage numero {i + 1} "] = listee
                print(f"Tirage triee numero {i + 1} " + str(listee))
            with open('sauvegarde-2.json', 'w') as f:
                # Écrit chaque ligne au format JSON dans le fichier
                json.dump(dictio, f)
                print("la liste Triee a bien était sauvegarder dans le fichier sauvegarde-2.json\n")

def ChargementListTriee_RechercheD_json(rech_d):
    if rech_d=="RechercheDichotomique":
        b = int(input("Quel nombre voulez vous connaitre sa position ?\n"))
        for i in range(0, x):
            charg = chargement_json('sauvegarde-2.json')[f"Tirage numero {i + 1} "]
            if type(rechercheDichotomique(charg, b)) == int:
                print(
                    f"le nombre {b} de la liste numero {i + 1} : se trouvant a la place numero {rechercheDichotomique(charg, b) + 1}")
            else:
                print(rechercheDichotomique(charg, b))
    elif  rech_d=="RechercheDichotomiqueRecursive" :
        b = int(input("Quel nombre voulez vous connaitre sa position ?\n"))
        for i in range(0, x):
            charg = chargement_json('sauvegarde-2.json')[f"Tirage numero {i + 1} "]
            if type(recherche_dichotomique_recursive(charg, b,0,len(charg))) == int:
                print(
                    f"le nombre {b} de la liste numero {i + 1} : se trouvant a la place numero {recherche_dichotomique_recursive(charg, b,0,len(charg)) + 1}")
            else:
                print(rechercheDichotomique(charg, b))


def SauvegardeEtChargementBinary(x):
    restd = {}
    # Exemple de liste
    for i in range(0, x):
        restd[f"Tirage numero {i + 1} "] = TirageLoto().tolist()
    # Ouvrir un fichier binaire en mode écriture
    with open("Sauvegarde.bin", "wb") as f:
        # Serialiser la liste en binaire et l'écrire dans le fichier
        pickle.dump(restd, f)
    restda = {}
    with open("Sauvegarde.bin", "rb") as f:
        # Désérialiser la liste à partir du fichier binaire
        restda = pickle.load(f)
    return restda

def Histogramme(valeurs):
    inter = []
    i=-0.5
    while i<46.5:

        inter.append(i)
        i=i+1

    plt.hist(valeurs, bins=inter, rwidth=0.8)  # Création de l'histogramme
    plt.xlabel('Valeurs')
    plt.xticks(n.arange(0, 46))
    plt.ylabel("Nombres d'occurences")
    plt.title("Histogramme ")
    plt.show()


if __name__ == '__main__':

    nb = int(input("combien voulez vous de tirage ?\n"))
    if nb>1000:
        x=1000
        print("""comme vous avez fait un tirage de plus de 10000 element cela mettrai trop de temp a etre triee, 
            je prendrai donc que 1000 liste  mais vous inquietez pas l'histogramme sera fait avec """, nb, "listes")
        time.sleep(1)
        input("tapez entrer si vous avez lus le paragraphe precedent")
    else: x=nb






    print("voici la sauvegarde du fichier en binaire et le chargement de celui ci : \n")
    print(SauvegardeEtChargementBinary(x),'\n')

    print("la sauvegarde et le chargement de ce fichier ont été faites\n")

    n.random.seed(0)
    a = input("comment voulez vous enregistrez votre fichier en csv ou json ?\n")

    if a == "csv" :

        sauvegarde_csv(x)
        print("la liste a bien était sauvegarder dans le fichier sauvegarde-1.csv\n")
        c = input("Quel  type de tri voulez vous TriCocktail, TriInsertion, TriFusion ?\n")
        #Difficultes parceque il faut pas ouvrir en lecture et aussi en ecriture
        Chargemement_Sauvegarde_Tri_csv(c, x)
        rech_d=input("Quel recherche voulez vous RechercheDichotomique ou RechercheDichotomiqueRecursive ?\n")
        ChargementListTriee_RechercheD_csv(rech_d)

    elif a == "json":

        sauvegarde_json(x)
        print("la liste a bien était sauvegarder dans le fichier sauvegarde-2.json\n")
        typeTri=input("Quel  type de tri voulez vous TriCocktail, TriInsertion, TriFusion ?\n")
        Chargemement_Sauvegarde_Tri_json(typeTri, x)
        rech_d = input("Quel recherche voulez vous RechercheDichotomique ou RechercheDichotomiqueRecursive ?\n")
        ChargementListTriee_RechercheD_json(rech_d)

    print("L'histogramme est entrain de se creer ...")
    print("si vous avez choisi 1 million l'histogramme mettra que environ 20 seconde, ne vous inquitez pas "
          "le programme a bien était optimiser pour ce genre d'operation ")
    listeee=[]
    listeee.extend(SauvegardeEtChargementBinary(nb).values())
    listeee=list(itertools.chain.from_iterable(listeee))
    Histogramme(listeee)










