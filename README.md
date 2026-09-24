# PyCryptoTool

**PyCryptoTool** est une application console interactive développée en **Python** permettant de manipuler différents algorithmes de chiffrement classiques, notamment le **Chiffre de César** et le **Chiffre XOR**.

## Fonctionnalités

- **Chiffrement de César** : chiffrez n'importe quel texte en spécifiant un décalage personnalisé.
- **Déchiffrement de César** : retrouvez le message original à partir du texte chiffré et de sa clé.
- **Attaque par force brute (César)** : testez automatiquement les 25 décalages possibles pour casser un message chiffré sans connaître le décalage.
- **Chiffrement et déchiffrement XOR** *(en cours de développement)* : implémentation basée sur l'opération logique XOR et une clé secrète.

## Prérequis

- Python **3.8** ou une version supérieure.

## Installation et utilisation

1. **Cloner le dépôt :**

```bash
   git clone https://github.com/david-mz/PyCryptoTool.git
   cd PyCryptoTool
```

2. **Lancer le programme :**

```bash
   python main.py
```

3. **Interagir avec le menu :** suivez les instructions affichées à l'écran pour choisir le type d'opération souhaité.

## Structure du projet

```text
PyCryptoTool/
│
├── main.py          # Script principal contenant les algorithmes et l'interface CLI
└── README.md        # Documentation du projet
```

## Évolutions futures

- [ ] Compléter l'implémentation du chiffrement/déchiffrement XOR.
- [ ] Ajouter la gestion des erreurs d'entrée utilisateur (ex. saisie de texte à la place d'un entier).
- [ ] Ajouter le chiffrement de Vigenère.

---

*Développé à des fins éducatives.*
