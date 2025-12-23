# 🎰 Projet Casino : Simulation Monte Carlo

Ce projet a pour objectif de vérifier l'équité des jeux de casino et de prouver mathématiquement que "la banque gagne toujours" sur le long terme via des simulations de masse.

---

## 📌 Étape actuelle : Niveau 1 - Le Prototype

Le but de ce premier palier était de coder la logique de base du jeu et de vérifier que les règles de gain et de perte fonctionnent correctement sur un petit échantillon.

### 🏗️ Caractéristiques Techniques

- **Langage :** Python 3.
- **Structure :** Boucle `while` de 10 itérations.
- **Logique :** Comparaison de deux tirages aléatoires entre 1 et 10.
- **Gestion du Capital :** Mise à jour en temps réel et détection de la ruine.

### 🚀 Fonctionnalités du Code

- Initialisation d'un capital de départ (100€).
- Tirage aléatoire sécurisé via la bibliothèque `random`.
- Affichage détaillé de chaque tour en console pour validation visuelle.
- Arrêt automatique si le solde atteint 0€ (Risque de Ruine).

---

## 📊 Analyse du ROI (Level 1)

Pour ce prototype, nous mesurons le Retour sur Investissement du temps de développement par rapport à la valeur technique produite :

$$ROI = \frac{Valeur\_du\_Prototype - Coût\_de\_Développement}{Coût\_de\_Développement}$$

> **Note :** Ce premier palier valide la viabilité du moteur avant le passage à 1 million de parties (Niveau 2).

---

## 🛠️ Comment lancer le script ?

1. **Prérequis :** Avoir Python installé sur sa machine.
2. **Clonage :**
   ```bash
   git clone [https://github.com/DaupinDavid/Roadmap.git](https://github.com/DaupinDavid/Roadmap.git)
3. **Exécution :** ```bash python casino_lvl1.py ```