#!/usr/bin/env python3
import sys
import csv

# Création du Mapper
def mapper():
    reader = csv.DictReader(sys.stdin)
    for row in reader:
        if len(row) == 25:  # Vérifier que la ligne a exactement 25 colonnes
            # Lire les données
            date = row['datcde']
            city = row['villecli']
            order_code = row['codcde']
            quantity = row['qte']
            timbrecde = row['timbrecde']
            cpcli = row['cpcli']

            if date and "-" in date:
                year = int(date.split("-")[0])
                if year >= 2006 and year <= 2010 and cpcli[:2] in ['53', '61', '28']:
                    print(f"{city},{order_code},{cpcli}\t{quantity},{timbrecde}")
            else:
                print(f"Skipping row with invalid date: {row}", file=sys.stderr)
        else:
            print(f"Saut de lignes car nombre de colonnes insuffisantes: {row}", file=sys.stderr)

# Exécuter le Mapper
if __name__ == "__main__":
    mapper()