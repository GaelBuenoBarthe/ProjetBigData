import pandas as pd
import unidecode

def read_and_clean_csv(file_path):
    # Lire le fichier CSV
    df = pd.read_csv(file_path)

    # Enlever les accents
    df = df.applymap(lambda x: unidecode.unidecode(x) if isinstance(x, str) else x)

    # Convertir les dates et enlever les lignes avec des dates invalides
    df['datcde'] = pd.to_datetime(df['datcde'], errors='coerce')
    df = df.dropna(subset=['datcde'])

    return df