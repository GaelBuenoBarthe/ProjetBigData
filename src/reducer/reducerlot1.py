#!/usr/bin/env python3
import sys
import heapq

# Création du Reducer
def reducer():
    current_key = None
    total_quantity = 0
    total_timbrecde = 0.0
    top_orders = []
    # Lire les données
    for line in sys.stdin:
        key, value = line.strip().split("\t")
        quantity, timbrecde = map(float, value.split(","))
        if current_key == key:
            total_quantity += quantity
            total_timbrecde += timbrecde
        else:
            if current_key:
                heapq.heappush(top_orders, (total_quantity, round(total_timbrecde, 2), current_key))
                if len(top_orders) > 100:
                    heapq.heappop(top_orders)
            current_key = key
            total_quantity = quantity
            total_timbrecde = timbrecde

    # Afficher les 100 meilleures commandes
    if current_key:
        heapq.heappush(top_orders, (total_quantity, round(total_timbrecde, 2), current_key))
        if len(top_orders) > 100:
            heapq.heappop(top_orders)

    # Afficher les résultats
    for quantity, timbrecde, key in sorted(top_orders, reverse=True):
        print(f"{key}\t{quantity},{timbrecde:.2f}")

if __name__ == "__main__":
    reducer()