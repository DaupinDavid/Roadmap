# Importation de la bibliothèque pour gérer le hasard
import random

# Fonction simulant le tirage d'une carte (entre 1 et 10)
def tirer_carte():
    nombre = random.randint(1, 10)
    return nombre

#Fonction principale du jeu
def jouer_partie(montant, mise):
    mon_score = tirer_carte()
    score_croupier = tirer_carte()
    if mon_score > score_croupier:
        montant_partie = round(mise, 2)
        msg = f"Félicitations! Tu as gagné {montant_partie:.2f}€!"
    elif mon_score == score_croupier:
        montant_partie = -round(mise / 2, 2)
        msg = f"Egalité. Ici, l'égalité te fais perdre {abs(montant_partie):.2f}€, la moitié de ta mise... "
    else: 
        montant_partie = -round(mise, 2)
        msg = f"Dommage... Tu as perdu {abs(montant_partie):.2f}€."
    montant += montant_partie
    montant = round(montant, 2)  
    return montant, msg, mon_score, score_croupier
    

# Configuration initiale du jeu
nom = input("Bienvenue au Casino! Quel est ton nom? ")
while True: # Boucle pour s'assurer que le montant est un entier positif
    try:
        montant = float(input(f"Salut {nom}! Combien souhaites-tu apporter au Casino aujourd'hui? (€) "))
        if montant > 0:
            break
        else:
            print("Veuillez entrer un montant au moins égal à 1.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
print(f"Félicitations {nom}! Tu démarres avec {montant:.2f}€.")
montant_depart = montant
mise = round(montant / 10, 2)  # Calcul de la mise par partie
print(f"Chaque partie coûtera {mise:.2f}€.")
parties_jouees = 0

# Simulation des 10 parties
print(f"Bonjour {nom}, tu rentres avec {montant:.2f}€. Il y aura 10 parties et chaque partie coûte {mise:.2f}€. Bonne chance!")
while parties_jouees < 10 :
    print(f"--- Partie Numéro {parties_jouees + 1} ---")
    montant, msg, mon_score, score_croupier = jouer_partie(montant, mise)
    print(f" Carte Croupier n° {score_croupier}")
    print(f" Carte {nom} n° {mon_score}")
    print(msg)
    parties_jouees += 1
    print(f"Tu dispose de {montant:.2f}€ ")

    # Vérification si le joueur est ruiné
    if montant <= 0:
        print ("Tu es ruiné... Le Casino te remercie et te souhaites une agréable journée. A bientôt!")
        break
gain_net = montant - montant_depart
roi = (gain_net / montant_depart)*100 if montant_depart != 0 else 0
if montant > 0:
    print(f"Fin du jeu! Tu repars avec {montant:.2f}€. Ton gain net est de {gain_net:.2f}€. ")
    print(f"Ton retour sur investissement est de {roi:.2f}% par rapport à ta mise initiale.")

print("Au revoir !")