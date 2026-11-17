"""Tests de la classe Bateau."""

from bateau import Bateau
from grille import Grille


def test_valeurs_par_defaut():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False


def test_positions_horizontal():
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]


def test_positions_vertical():
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [
        (2, 3),
        (3, 3),
        (4, 3),
    ]


def test_pas_coule():
    g = Grille(5, 8)
    b = Bateau(2, 3, longueur=3)
    g.ajoute(b)
    assert b.coule(g) is False

    g.tirer(2, 3)
    assert b.coule(g) is False


def test_coule():
    g = Grille(5, 8)
    b = Bateau(2, 3, longueur=3)
    g.ajoute(b)
    for ligne, colonne in b.positions():
        g.tirer(ligne, colonne)
    assert b.coule(g) is True
