"""Bateaux de la bataille navale."""


class Bateau:
    """Un bateau est une ligne de `longueur` cases, horizontale ou non."""

    #: marque par défaut d'un bateau sur la grille
    marque = "⛵"

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        """ligne et colonne sont obligatoires, le reste a une valeur par défaut."""
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        """Rend la liste des cases occupées, sous forme de couples (ligne, colonne)."""
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def coule(self, grille):
        """Vrai si toutes les cases du bateau ont été touchées sur la grille.

        Une case est « touchée » dès qu'elle ne porte plus ni la marque du
        bateau ni le caractère de case vierge : cela couvre aussi bien le
        'x' par défaut que le "💣" utilisé par le jeu.
        """
        for ligne, colonne in self.positions():
            case = grille.grille[grille.indice(ligne, colonne)]
            if case in (grille.vide, self.marque):
                return False
        return True

    # Le sujet écrit « coulé » avec un accent : on expose les deux noms.
    coulé = coule
