"""Tests de la classe Grille."""

from bateau import Bateau
from grille import Grille


def test_init():
    g = Grille(5, 8)
    assert g.lignes == 5
    assert g.colonnes == 8
    assert len(g.grille) == 40
    assert g.grille == [g.vide] * 40


def test_str_grille_vide():
    g = Grille(5, 8)
    attendu = "\n".join(["." * 8 for _ in range(5)])
    assert str(g) == attendu


def test_tirer():
    g = Grille(5, 8)
    g.tirer(2, 3)
    assert g.grille[2 * 8 + 3] == "x"
    assert str(g).splitlines()[2] == "...x...."


def test_tirer_avec_touche():
    g = Grille(5, 8)
    g.tirer(1, 1, touche="💣")
    assert g.grille[1 * 8 + 1] == "💣"


def test_ajoute_horizontal():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.grille == ["∿", "∿", "∿", "⛵", "⛵", "∿"]


def test_ajoute_ne_rentre_pas():
    g = Grille(2, 3)
    avant = list(g.grille)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.grille == avant
