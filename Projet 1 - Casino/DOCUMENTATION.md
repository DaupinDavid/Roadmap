# 📄 Documentation Technique — Level 1

## 🎰 Projet Casino : Modélisation du Risque de Ruine

> Démonstration empirique qu’un jeu à espérance négative mène mécaniquement à la ruine sur le long terme.

---

## 1️⃣ Logique Technique

**Langage :** Python 3.10+  
**Bibliothèque :** `random`  
**Méthode :** Boucle `while` avec double condition d’arrêt :

- Nombre de tours atteint (10 pour Level 1)
- Ruine du joueur (capital ≤ 0)

**Algorithme :**

1. Tirage aléatoire d’une carte pour le joueur et le croupier.
2. Comparaison des scores.
3. Mise à jour du capital selon les règles :
   - Victoire (+10€)
   - Défaite (-10€)
   - Égalité (-5€, avantage maison)
4. Vérification de la ruine du joueur.
5. Affichage des résultats et capital actuel.

**Choix technique :**

- Exécution instantanée (<0.01s) pour valider le prototype avant simulation de masse.
- Le moteur de hasard génère une distribution uniforme discrète sur l'intervalle `[1, 10]`. Les tirages sont considérés comme i.i.d. (Indépendants et Identiquement Distribués), garantissant la stabilité statistique du modèle.
- Structure simple et lisible pour faciliter le debugging.

---

## 2️⃣ Justification / Analyse Métier

- La roulette intègre un **avantage structurel** (ici : l’égalité prélève 50% de la mise).
- L’espérance négative entraîne une **convergence statistique vers la ruine** du joueur.
- Level 1 : validation de la logique algorithmique.
- Level 2 : simulation de masse pour observer la loi des grands nombres.
- Level 3 : optimisation pour haute performance.

---

## 3️⃣ Espérance Mathématique (E)

Pour chaque tour de jeu (tirage 1-10) :

$$
E = (0.45 \times 10) + (0.10 \times -5) + (0.45 \times -10) = -0,5\€ / \text{tour}
$$
Interprétation : le joueur perd en moyenne 0,50 € par tour.
Conclusion : confirme l’avantage structurel du casino et la non-viabilité du jeu à long terme.

4️⃣ Limites & Hypothèses
Prototype limité à 10 tours.

Données pseudo-aléatoires (bibliothèque random).

Capital initial fixe à 100€.

Pas de stratégies complexes de mise.

Simulation de masse et optimisation prévues pour Level 2 et 3.


**Ce projet démontre empiriquement et mathématiquement qu’un jeu à espérance négative mène à la ruine sur le long terme.**