from utils import read_and_clean_csv
import os

def lot1(file_path, output_dir):
    df = read_and_clean_csv(file_path)

    # Filtrer les données entre 2006 et 2010 et pour les départements 53, 61, et 28
    df = df[(df['datcde'].dt.year >= 2006) & (df['datcde'].dt.year <= 2010)]
    df = df[df['cpcli'].astype(str).str[:2].isin(['53', '61', '28'])]

    # Ajouter la colonne codedptmt
    df['codedptmt'] = df['cpcli'].astype(str).str[:2]

    # Calculer les 100 meilleures commandes
    top_orders = df.groupby(['villecli', 'codcde', 'codedptmt']).agg({
        'qte': 'sum',
        'timbrecde': 'sum'
    }).reset_index()

    top_orders = top_orders.sort_values(by=['qte', 'timbrecde'], ascending=False).head(100)

    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Exporter le résultat dans un fichier Excel
    output_file = os.path.join(output_dir, 'top_100_cde_lot1.xlsx')
    top_orders.to_excel(output_file, index=False)

    print(f"Les résultats ont été exportés dans {output_file}")

if __name__ == "__main__":
    file_path = 'data/clean/dataw_fro03_clean.csv'
    output_dir = 'data/output'
    lot1(file_path, output_dir)