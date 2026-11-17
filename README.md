# Projet bataille navale

Version simplifiée de la bataille navale : une grille de 8 lignes et 10
colonnes, quatre bateaux placés au hasard, et un joueur qui tire jusqu'à
ce qu'ils soient tous coulés.

## Installation

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Windows cmd
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Lancer les tests

```bash
pytest -q
```

## Lancer le jeu

```bash
python main.py
```

Le jeu demande `colonne ligne` (par exemple `3 4` pour la colonne 3, ligne 4).
`q` abandonne la partie.

Légende de l'affichage : `.` case inconnue, `x` tir dans l'eau, `💣` bateau
touché, marque d'un bateau = bateau coulé (il est alors révélé).

Les couleurs viennent de `termcolor` et ne s'affichent que dans un vrai
terminal (pas quand la sortie est redirigée vers un fichier).

## Organisation des fichiers

| Fichier | Rôle |
| --- | --- |
| `grille.py` | la classe `Grille` : tirs, placement, affichage |
| `bateau.py` | la classe `Bateau` : positions, coulé |
| `bateaux_specifiques.py` | les quatre types de bateaux (longueur et marque) |
| `main.py` | le jeu complet |
| `story_grille.py` | user story « Plouf dans l'eau » |
| `story_bateau.py` | user story « chevauchement » |
| `test_grille.py` | tests de la grille |
| `test_bateau.py` | tests du bateau |
| `test_bateaux_specifiques.py` | tests des types de bateaux |

## Conventions

- Une case vierge vaut `Grille.vide` (`"∿"`), mais `__str__` l'affiche `.`.
- Une case touchée vaut `"x"` par défaut, `"💣"` quand le tir touche un bateau.
- L'indice de la case `(ligne, colonne)` dans `Grille.grille` est
  `ligne * colonnes + colonne`.
- Les bateaux cachés ne sont révélés qu'une fois coulés (leur marque apparaît).

## Diagrammes UML

Les diagrammes sont dans `uml/` :

- `01-grille-sans-bateaux.png` — la grille seule
- `02-grille-complete.png` — la grille avec `vide`, `indice` et les états de case
- `03-bateaux.png` — `Bateau`, ses quatre sous-classes et leurs liens avec `Grille`

La source PlantUML est `uml/diagrammes.puml` (à ouvrir sur
[plantuml.com](https://www.plantuml.com/plantuml/) ou avec l'extension
PlantUML de VS Code pour régénérer les images).

## Types de bateaux

| Type | Longueur | Marque |
| --- | --- | --- |
| Porte-avions | 4 | 🚢 |
| Croiseur | 3 | ⛴ |
| Torpilleur | 2 | 🚣 |
| Sous-marin | 2 | 🐟 |
