# Importation de la bibliothèque pour gérer le hasard
import random

# Fonction simulant le tirage d'une carte (entre 1 et 10)
def tirer_carte():
    nombre = random.randint(1, 10)
    return nombre

# Configuration initiale du jeu
nom = "Joueur"
montant = 100
montant = int(montant)
partie_jouées = 0

# Simulation des 10 parties
print(f"Bonjour {nom}, tu rentres avec {montant}€")
while partie_jouées < 10 :
    print(f"--- Partie Numéro {partie_jouées + 1} ---")
    mon_score = tirer_carte()
    print(f"Tu as tiré la carte n° {mon_score}")
    score_croupier = tirer_carte()
    print(f"Le croupier a tiré la carte n° {score_croupier}")

    # Détermination du gagnant et mise à jour du montant
    if mon_score > score_croupier:
        montant = (montant + 10)
        print(f"Félicitations! Tu as gagné 10€! | Score Croupier: {score_croupier} | Ton Score: {mon_score}") 
    elif mon_score == score_croupier:
        montant = (montant - 5)
        print(f"Egalité. Ici, l'égalité te fais perdre la moitié de ta mise... | Score Croupier: {score_croupier} | Ton Score: {mon_score}")
    else: 
        montant = (montant - 10)
        print(f"Dommage... Tu as perdu 10€. | Score Croupier: {score_croupier} | Ton Score: {mon_score}")
    partie_jouées = partie_jouées + 1
    print(f"Tu dispose de {montant}€ ")

    # Vérification si le joueur est ruiné
    if montant <= 0:
        print ("Tu es ruiné... Le Casino te remercie et te souhaites une agréable journée. A bientot!")
        break
print("Au revoir !")