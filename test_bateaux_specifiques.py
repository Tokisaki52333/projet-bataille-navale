"""Tests des types de bateaux."""

import pytest

from bateaux_specifiques import Croiseur, PorteAvion, SousMarin, Torpilleur
from grille import Grille


@pytest.mark.parametrize(
    "classe, longueur, marque",
    [
        (PorteAvion, 4, "🚢"),
        (Croiseur, 3, "⛴"),
        (Torpilleur, 2, "🚣"),
        (SousMarin, 2, "🐟"),
    ],
)
def test_caracteristiques(classe, longueur, marque):
    b = classe(0, 0, False)
    assert b.longueur == longueur
    assert b.marque == marque
    assert len(b.positions()) == longueur


def test_ajout_type_sur_grille():
    g = Grille(8, 10)
    g.ajoute(Croiseur(1, 2, False))
    assert g.grille[1 * 10 + 2] == "⛴"
    assert g.grille[1 * 10 + 4] == "⛴"
    assert g.grille[1 * 10 + 5] == "∿"
