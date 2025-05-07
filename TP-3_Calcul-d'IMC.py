#fonction pour calculer l'imc
def calculer_imc(poids,taille):
    imc = poids /(taille** 2)
    return imc

#l'utilisateur insert ses données
poids = float(input("Quel est votre poids en Kg : "))
taille = float(input("Quel est votre Taille en m : "))

#on redefinis le calcul
imc =calculer_imc(poids, taille)
if imc < 18.5 :
   resultat = "votre Poids est insuffisant "
elif 18.5 <= imc <= 25 :
   resultat = "votre Poids est Normal "
elif 25 <= imc < 30 :
   resultat = "vous êtes en Surpoids"
elif imc >= 30 :
   resultat = "vous êtes en Obésité"

#Le resultat
print (f"Votre Imc est de {imc:.2f} C'est à dire que {resultat}")
#.2f == prend uniquement les 2 valeur après le point (pour mieux arrondir)
