import pandas as pd
import numpy as np
from IPython.display import display

class Analyst():
    """docstring for Analyst."""
    def __init__(self, src: str, delimiter :str = ","):
        self.src = src
        self.delimiter = delimiter
    
    def start_analyse(self) -> pd.DataFrame :
        """
        Charge un fichier brut (CSV ou Excel) et affiche un diagnostic rapide.

        """
        try:
            if self.src.endswith(".csv"):
                # 1. Chargement du fichier 
                df = pd.read_csv(self.src, sep= self.delimiter, encoding='utf-8', low_memory=False)
                # 2. Gestion des fichiers Excel
            elif self.src.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(self.src, sep=self.delimiter,low_memory=False )
            else:
                raise ValueError("Format de fichier non reconnu. Utilisez .csv ou .xlsx")
            # 3. Le mini-diagnostic (très utile pour vérifier que le délimiteur était le bon)
            print("Fichier chargé avec succès !")
           # print(df.info())
            print(f"Dimensions : {df.shape[0]} lignes | {df.shape[1]} colonnes")
            print("-" * 40)
            #Compter le nombre de valeurs nulles
            print("Chargement du nombre de valeurs nulles pour ce fichier! ")
            display(df.isnull().sum())
            print("-" * 40)
            print("Chargement des 5 premières lignes du fichier")
            display(df.head(5))
            print("-" * 40)
            return df

        except Exception as e:
            print(f" Erreur lors du chargement : {e}")
            # Si le fichier ne charge pas, on renvoie un DataFrame vide pour ne pas faire planter la suite
            return pd.DataFrame()
        
