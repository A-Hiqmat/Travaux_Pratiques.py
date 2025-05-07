# Objectif : Afficher l'identité d'une personne : 
    # "Nom", "Prenom", "age", "age_an_prochain"

# Etape-1 : Déclaration des variables
    # Variables : nom, prenom, age, age_an_prochain
nom = input("Quel est votre nom ? : ")
prenom = input("Quel est votre prénom ? : ")
age = int(input("Quel est votre âge ? : "))

# Etape-2 : 
    # Print-1 : afficher l'identité avec (Nom, Prenom, Age)
    # Print-2 : "L'an prochain vous aurez " ?
print(f"Vous vous appelez {nom} {prenom} et vous avez {age} ans.")
print(f"L'an prochain vous aurez {age+1}")