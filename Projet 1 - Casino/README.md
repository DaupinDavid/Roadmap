````markdown
# 🎰 Projet Casino : Modélisation du Risque de Ruine

> Démonstration empirique qu’un jeu à espérance négative mène mécaniquement à la ruine sur le long terme.

---

## 📊 Progression du Projet

- **Level 1 : Prototype / Logique de base** ✅
- **Level 2 : Simulation de masse / Complexité** 🏗️
- **Level 3 : Optimisation / Haute Performance** ⏳

---

## 🔹 Objectif

Valider par simulation que, malgré des gains ponctuels, l’avantage statistique du casino conduit à la ruine du joueur.  
Illustration de la **non-viabilité d’un système à espérance négative**.

---

## 🎲 Mécanique du Level 1

- Tirage aléatoire d’une carte (1 à 10) pour le joueur et le croupier.
- **Victoire (+10€)** : joueur > croupier
- **Défaite (-10€)** : joueur < croupier
- **Égalité (-5€)** : le casino prélève 50% de la mise (avantage maison)

---

## 🚀 Exécution rapide

```bash
python src/casino_lvl1.py
```
````

---

## 🔹 Résultats observés

- **Performance :** Exécution complète en < 0.01s
- **Mécanisme :** Débit automatique du capital à chaque perte ou égalité
- **Sécurité :** Arrêt immédiat du script si capital ≤ 0
- **Intégrité :** Validation de la logique algorithmique avant simulation de masse (Level 2)

---

## 📉 Preuve mathématique

Espérance négative du Level 1 :

$$
E = (0.45 \times 10) + (0.10 \times -5) + (0.45 \times -10) = - 0,5 €/\text{tour}
$$

> En moyenne, le joueur perd 0,50€ par tour, confirmant l’avantage structurel du casino.

---

## 📄 Documentation complète

Pour les détails techniques, analyses métier et limites, voir [DOCUMENTATION.md](DOCUMENTATION.md).

---

**Ce projet démontre empiriquement et mathématiquement qu’un jeu à espérance négative mène à la ruine sur le long terme.**

```

```
