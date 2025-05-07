#creation d'une liste recette vide
recette = []

#Créez une fonction afficher_ingredient(recette) qui affiche la liste des ingredient de la recette
def afficher_ingredient():
    if not recette :
        print("Aucun ingredient dans la liste! Veillez à en rajouter :)")
    else:
        print("\nListe de recette : ")
        for i, recettes in enumerate(recette,start=1) :
            print(f"{i}. {recettes}")


#Créez une fonction ajouter_ingredient(recette) qui demande un ingrédient à l'utilisateur et l’ajoute à la liste.
def ajouter_ingredient():
    nouvel_ingredient = input("Quel ingredient souhaitez vous ajouter ? : ")
    recette.append(nouvel_ingredient)
    print("ingredient " + nouvel_ingredient + " ajouté avec succès." )

#Nous permet de supprimer un ingredient
def supprimer_ingredient(): 
    afficher_ingredient()
    if recette :
        try:
            indice = int(input("Entrez le numéro de l'ingrédient à supprimer : "))
            if 1 <= indice <= len(recette):
                supprimer_ingredient = recette.pop(indice - 1)
                print(f"Tâche '{supprimer_ingredient}' supprimée avec succès.")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

# Boucle du Menu
def menu():
# Affiche un menu qui permet de gérer la recette.
    while True:
        print("\nMenu :")
        print("1. Ajouter un ingrédient")
        print("2. Afficher la recette")
        print("3. Supprimer un ingrédient")
        print("4. Quitter")
        
        choix = input("Choisissez une option (1-4) : ")
        if choix == "1":
            ajouter_ingredient()
        elif choix == "2":
            afficher_ingredient()
        elif choix == "3":
            supprimer_ingredient()
        elif choix == "4":
            print("Vous allez sortir du menu !")
            break
        else:
            print("Action impossible. Veuillez choisir une option entre 1 et 4.")

# Lancer le menu
menu()