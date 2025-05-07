# Saisie du nombre d'articles
nombre_articles = int(input("Combien d'articles souhaitez-vous ajouter à la facture ? "))

# Calcul du tresulta
total = 0
for i in range ( nombre_articles) : 
# on incremente
    prix = float(input(f"Entrez le prix de l'article { i+1} : "))
    total += prix

# Etape 3 : on applique la réduction si l'argent arrive à 100$
if total > 100 :
    reduction = total * 0.10
    total -= reduction
    print(f"Une réduction de 10% vous a été appliqué : -{reduction:.2f}€.Le montant total de votre facture est : {total:.2f}€. ")
#Etape 4: sinon on affiche les autres resultats
else :
   print(f"Le montant total de votre facture est : {total:.2f}€.")