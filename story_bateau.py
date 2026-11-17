"""User story "chevauchement".

- Nom : "chevauchement"
- Utilisateur : un joueur
- Story : Positionner des bateaux sans chevauchement
- Actions :
    1. créer un bateau b1
    2. créer un bateau b2
    3. vérifier si les deux bateaux se chevauchent
"""

from bateau import Bateau


def chevauche(b1, b2):
    return bool(set(b1.positions()) & set(b2.positions()))


def main():
    # jeu d'essai 1 : les bateaux se chevauchent
    b1 = Bateau(2, 3, longueur=3)  # (2,3) (2,4) (2,5)
    b2 = Bateau(2, 5, longueur=2)  # (2,5) (2,6)
    print("Chevauchement attendu True :", chevauche(b1, b2))

    # jeu d'essai 2 : les bateaux ne se chevauchent pas
    b3 = Bateau(2, 3, longueur=3)  # (2,3) (2,4) (2,5)
    b4 = Bateau(2, 6, longueur=2)  # (2,6) (2,7)
    print("Chevauchement attendu False :", chevauche(b3, b4))


if __name__ == "__main__":
    main()
