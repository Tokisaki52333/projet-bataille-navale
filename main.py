"""Le jeu de bataille navale.

Grille de 8 lignes et 10 colonnes, quatre bateaux (un de chaque type)
placés au hasard sans chevauchement. Le joueur tire jusqu'à ce que
tous les bateaux soient coulés, puis on affiche le nombre de coups.
"""

import random

try:
    from termcolor import colored
except ImportError:  # termcolor reste optionnel : le jeu marche sans
    def colored(text, *args, **kwargs):
        return text

from bateaux_specifiques import Croiseur, PorteAvion, SousMarin, Torpilleur
from grille import Grille

LIGNES = 8
COLONNES = 10


def placements_possibles(grille, bateau_cls):
    """Rend tous les couples (ligne, colonne, vertical) où un bateau de
    classe `bateau_cls` tient sans sortir de la grille et sans chevaucher
    un bateau déjà placé.
    """
    possibles = []
    for ligne in range(grille.lignes):
        for colonne in range(grille.colonnes):
            for vertical in (False, True):
                bateau = bateau_cls(ligne, colonne, vertical=vertical)
                positions = bateau.positions()
                if all(
                    grille.dans_grille(ligne_bateau, colonne_bateau)
                    and grille.grille[grille.indice(ligne_bateau, colonne_bateau)]
                    == grille.vide
                    for ligne_bateau, colonne_bateau in positions
                ):
                    possibles.append((ligne, colonne, vertical))
    return possibles


def place_aleatoirement(grille, classes_bateaux):
    """Place les bateaux un par un, en tirant au hasard parmi les
    placements possibles à chaque étape. Rend la liste des bateaux placés.
    """
    bateaux = []
    for bateau_cls in classes_bateaux:
        possibles = placements_possibles(grille, bateau_cls)
        if not possibles:
            raise RuntimeError(f"Impossible de placer {bateau_cls.__name__}")
        ligne, colonne, vertical = random.choice(possibles)
        bateau = bateau_cls(ligne, colonne, vertical=vertical)
        grille.ajoute(bateau)
        bateaux.append(bateau)
    return bateaux


def demande_tir(grille):
    """Demande deux coordonnées au joueur et rend le couple (ligne, colonne)."""
    while True:
        entree = input(colored("Entrez colonne et ligne (ex: 3 4), ou q pour quitter : ", "cyan"))
        if entree.strip().lower() == "q":
            return None
        try:
            x_str, y_str = entree.split()
            colonne = int(x_str)
            ligne = int(y_str)
        except ValueError:
            print(colored("Entrée invalide. Donnez deux entiers séparés par un espace.", "yellow"))
            continue
        if not grille.dans_grille(ligne, colonne):
            print(colored("Coordonnées hors de la grille.", "yellow"))
            continue
        return ligne, colonne


def bateau_sur_case(bateaux, ligne, colonne):
    for bateau in bateaux:
        if (ligne, colonne) in bateau.positions():
            return bateau
    return None


def joue():
    """Déroule une partie complète."""
    grille = Grille(LIGNES, COLONNES)
    classes = [PorteAvion, Croiseur, Torpilleur, SousMarin]
    bateaux = place_aleatoirement(grille, classes)
    # On masque les bateaux sur la grille affichée au joueur.
    # La grille interne garde les marques pour la logique; l'affichage joueur
    # montrera les tirs. Pour cela on garde une vue "publique".
    grille_publique = Grille(LIGNES, COLONNES)

    coups = 0
    deja_tires = set()
    bateaux_coules = set()

    print(colored("=== Bataille navale ===", "magenta", attrs=["bold"]))
    print("Tirez sur les cases (colonne ligne). Les bateaux sont cachés.")
    print("Légende: . = inconnu, x = plouf, 💣 = touché, marque = bateau coulé")

    while len(bateaux_coules) < len(bateaux):
        print()
        print(grille_publique)
        tir = demande_tir(grille_publique)
        if tir is None:
            print(colored("Partie abandonnée.", "red"))
            return
        ligne, colonne = tir
        if (ligne, colonne) in deja_tires:
            print(colored("Vous avez déjà tiré ici.", "yellow"))
            continue

        deja_tires.add((ligne, colonne))
        coups += 1
        bateau = bateau_sur_case(bateaux, ligne, colonne)

        if bateau is None:
            grille_publique.tirer(ligne, colonne, touche="x")
            print(colored("Plouf !", "blue"))
            continue

        # Touché
        grille.tirer(ligne, colonne, touche="💣")
        grille_publique.tirer(ligne, colonne, touche="💣")
        print(colored("Touché !", "red", attrs=["bold"]))

        if bateau.coule(grille):
            bateaux_coules.add(id(bateau))
            # Révéler le bateau coulé sur la grille publique avec sa marque
            for ligne_bateau, colonne_bateau in bateau.positions():
                indice = grille_publique.indice(ligne_bateau, colonne_bateau)
                grille_publique.grille[indice] = bateau.marque
            message = getattr(
                bateau, "message_coule", f"{bateau.__class__.__name__} coulé !"
            )
            print(colored(message, "green", attrs=["bold"]))
        # Bateaux restants
        restants = len(bateaux) - len(bateaux_coules)
        if restants:
            print(colored(f"Bateaux restants : {restants}", "cyan"))

    print()
    print(grille_publique)
    print(colored(f"Victoire ! Tous les bateaux sont coulés en {coups} coups.",
                  "green", attrs=["bold"]))


if __name__ == "__main__":
    joue()
