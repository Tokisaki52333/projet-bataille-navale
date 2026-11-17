"""User story "Plouf dans l'eau".

- Nom : "Plouf dans l'eau"
- Utilisateur : un joueur
- Story : On veut pouvoir gérer les tirs de l'adversaire
- Actions :
    1. créer une grille à 5 lignes et 8 colonnes
    2. afficher la grille à l'écran
    3. demander à l'utilisateur de rentrer deux coordonnées x et y
    4. tirer à l'endroit indiqué sur la grille
    5. retour en 2
"""

from grille import Grille


def main():
    # 1. créer la grille
    grille = Grille(5, 8)
    while True:
        # 2. afficher la grille
        print(grille)
        # 3. demander x et y
        entree = input("coordonnées x y (ou q pour quitter) ? ")
        if entree.strip().lower() == "q":
            break
        try:
            x_str, y_str = entree.split()
            x = int(x_str)
            y = int(y_str)
        except ValueError:
            print("Entrée invalide, recommencez.")
            continue
        # 4. tirer
        grille.tirer(y, x)
        # 5. retour en 2


if __name__ == "__main__":
    main()
