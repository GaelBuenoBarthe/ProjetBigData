import subprocess

# Chemins vers les scripts et données
csv_file = 'data/clean/dataw_fro03_clean.csv'
mapper_script = 'src/mapper/mapperlot1.py'
reducer_script = 'src/reducer/reducerlot1.py'

# Exécuter le Mapper
with open(csv_file, 'r') as f:
    mapper_output = subprocess.run(['python', mapper_script], stdin=f, capture_output=True, text=True)

# Trier la sortie du Mapper
sorted_output = sorted(mapper_output.stdout.splitlines())

# Exécuter le Reducer
reducer_input = '\n'.join(sorted_output)
reducer_output = subprocess.run(['python', reducer_script], input=reducer_input, capture_output=True, text=True)

# Afficher la sortie du Reducer
print(reducer_output.stdout)