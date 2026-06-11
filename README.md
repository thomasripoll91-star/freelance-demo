# ⚽ Projet d'Analyse : Nettoyage de données FIFA 21

Ce projet est une démonstration pratique d'analyse et de nettoyage de données avec Python et Pandas. L'objectif est de traiter un jeu de données brut contenant de nombreuses incohérences (valeurs manquantes, types de données mixtes) afin de s'entraîner aux opérations d'exploration et de Data Cleaning.

## 📂 Structure du projet

\`\`\`text
📁 Racine du projet
├── 📁 scripts/
│   ├── 📄 function_analyst.py         # Contient la classe `Analyst` pour l'import et le diagnostic
│   └── 📓 Jupyter_analyse_exec.ipynb  # Notebook interactif pour l'exploration visuelle
└── 📁 data/
    └── 📊 fifa21.csv                  # Dataset brut à analyser
\`\`\`

## 📊 À propos des données

Le jeu de données utilisé est le fichier **fifa21.csv**. 
* **Dimensions :** 18 979 lignes | 77 colonnes
* **Défis techniques :** Le fichier génère des avertissements de types mixtes lors du chargement (`DtypeWarning`) et contient de nombreuses valeurs nulles nécessitant une stratégie de nettoyage ciblée.

## 🛠️ Prérequis

Pour exécuter ce projet, vous aurez besoin de l'environnement suivant :
* **Python 3.x**
* **Pandas** (Manipulation et nettoyage des données)
* **NumPy** (Calculs numériques)
* **Jupyter** (Pour l'affichage interactif de données complexes)

## 🚀 Utilisation

La logique principale du projet repose sur la classe orientée objet `Analyst`. Elle se charge de lire les fichiers de manière sécurisée (CSV ou Excel) et d'afficher un premier diagnostic de la qualité des données (dimensions, comptage des valeurs nulles, etc.).

**Exemple d'exécution dans le Notebook Jupyter :**

\`\`\`python
# Importation de la classe depuis le dossier scripts
from scripts.function_analyst import Analyst

# Initialisation avec le chemin vers les données
analyste = Analyst("data/fifa21.csv")

# Lancement du diagnostic et récupération du DataFrame
df = analyste.start_analyse()
\`\`\`