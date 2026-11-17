"""Grille de bataille navale.

La grille est une matrice L x C stockée dans une simple liste de
caractères : la case (ligne l, colonne c) se trouve à l'indice
l * colonnes + c.

Codes utilisés sur la grille :
- Grille.vide  : case jamais tirée
- 'x'          : case touchée (valeur par défaut de tirer)
- la marque d'un bateau : case occupée par un bateau
"""


class Grille:
    """Le terrain de jeu."""

    #: caractère d'une case vierge
    vide = "∿"

    def __init__(self, lignes, colonnes):
        """Crée une grille de `lignes` lignes et `colonnes` colonnes."""
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [self.vide] * (lignes * colonnes)

    def indice(self, ligne, colonne):
        """Indice dans self.grille de la case (ligne, colonne)."""
        return ligne * self.colonnes + colonne

    def dans_grille(self, ligne, colonne):
        return 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes

    def tirer(self, ligne, colonne, touche="x"):
        """Marque la case (ligne, colonne) comme touchée."""
        if self.dans_grille(ligne, colonne):
            self.grille[self.indice(ligne, colonne)] = touche

    def ajoute(self, bateau):
        """Place `bateau` sur la grille avec sa marque.

        Le bateau n'est placé que s'il rentre entièrement dans la grille
        et si aucune de ses cases n'est déjà occupée. Sinon la grille
        reste inchangée.
        """
        positions = bateau.positions()
        for ligne, colonne in positions:
            if not self.dans_grille(ligne, colonne):
                return
            if self.grille[self.indice(ligne, colonne)] != self.vide:
                return
        for ligne, colonne in positions:
            self.grille[self.indice(ligne, colonne)] = bateau.marque

    def __str__(self):
        """Rend la grille sous forme de texte, une ligne par ligne.

        Une case vide est affichée '.', les autres caractères sont
        affichés tels quels.
        """
        lignes = []
        for ligne in range(self.lignes):
            debut = ligne * self.colonnes
            fin = debut + self.colonnes
            ligne_txt = "".join(
                "." if case == self.vide else case
                for case in self.grille[debut:fin]
            )
            lignes.append(ligne_txt)
        return "\n".join(lignes)
