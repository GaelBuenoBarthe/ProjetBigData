import pandas as pd
import unidecode

def read_and_clean_csv(file_path):
    # Lire le fichier CSV
    df = pd.read_csv(file_path)

    # Enlever les accents uniquement pour les colonnes de type objet (chaînes de caractères)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].apply(lambda x: unidecode.unidecode(x) if isinstance(x, str) else x)

    # Convertir les dates et enlever les lignes avec des dates invalides
    df['datcde'] = pd.to_datetime(df['datcde'], errors='coerce')

    # Remplacer les valeurs non-finies par des valeurs par défaut appropriées
    df['codcli'] = df['codcli'].fillna(0).astype('int32')
    df['genrecli'] = df['genrecli'].fillna('').astype('string')
    df['nomcli'] = df['nomcli'].fillna('').astype('string')
    df['prenomcli'] = df['prenomcli'].fillna('').astype('string')
    df['cpcli'] = df['cpcli'].fillna('').astype('string').str.zfill(5)
    df['villecli'] = df['villecli'].fillna('').astype('string')
    df['codcde'] = df['codcde'].fillna(0).astype('int32')
    df['timbrecli'] = df['timbrecli'].fillna(0.0).astype(float)
    df['timbrecde'] = df['timbrecde'].fillna(0.0).astype(float)
    df['Nbcolis'] = df['Nbcolis'].fillna(0).astype('int8')
    df['cheqcli'] = df['cheqcli'].fillna(0.0).astype(float)
    df['barchive'] = df['barchive'].fillna(False).astype('bool')
    df['bstock'] = df['bstock'].fillna(False).astype('bool')
    df['codobj'] = df['codobj'].fillna(0).astype('int32')
    df['qte'] = df['qte'].fillna(0).astype('int16')
    df['Colis'] = df['Colis'].fillna(0).astype('int32')
    df['libobj'] = df['libobj'].fillna('').astype('string')
    df['Tailleobj'] = df['Tailleobj'].fillna('').astype('string')
    df['Poidsobj'] = df['Poidsobj'].fillna(0.0).astype(float)
    df['points'] = df['points'].fillna(0).astype('int32')
    df['indispobj'] = df['indispobj'].fillna(False).astype('bool')
    df['libcondit'] = df['libcondit'].fillna('').astype('string')
    df['prixcond'] = df['prixcond'].fillna(0.0).astype(float)
    df['puobj'] = df['puobj'].fillna(0.0).astype(float)

    return df