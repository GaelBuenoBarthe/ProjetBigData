from utils import read_and_clean_csv

# Netttoyer les données
def clean_data(file_path, output_path):
    df = read_and_clean_csv(file_path)
    df.to_csv(output_path, index=False)
    return df

# Sauvegarder les données nettoyées
if __name__ == "__main__":
    input_file_path = 'data/raw/dataw_fro03.csv'
    output_file_path = 'data/clean/dataw_fro03_clean.csv'
    df = clean_data(input_file_path, output_file_path)
    print(f"Les données nettoyées ont été sauvegardées dans {output_file_path}")
    print(df.head())