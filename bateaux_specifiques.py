"""Les quatre types de bateaux du jeu."""

from bateau import Bateau


class PorteAvion(Bateau):
    marque = "🚢"
    longueur_bateau = 4
    message_coule = "Le porte-avions est coulé !"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=self.longueur_bateau, vertical=vertical)


class Croiseur(Bateau):
    marque = "⛴"
    longueur_bateau = 3
    message_coule = "Le croiseur est coulé !"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=self.longueur_bateau, vertical=vertical)


class Torpilleur(Bateau):
    marque = "🚣"
    longueur_bateau = 2
    message_coule = "Le torpilleur est coulé !"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=self.longueur_bateau, vertical=vertical)


class SousMarin(Bateau):
    marque = "🐟"
    longueur_bateau = 2
    message_coule = "Le sous-marin est coulé !"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=self.longueur_bateau, vertical=vertical)
