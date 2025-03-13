import random
import re

# 📌 Chemins des fichiers
input_file = r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\merged_text.txt"  
output_file = "filtered_text.txt"

# 🔹 Étape 1 : Lire le fichier
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 🔹 Étape 2 : Tronquer 35 % des textes aléatoirement
num_lines = len(lines)
selected_lines = random.sample(lines, int(num_lines * 0.35))  # Prendre 35 %

# 🔹 Étape 3 : Nettoyer les textes
def clean_text(text):
    text = re.sub(r"\s+", " ", text)  # Supprimer les espaces multiples
    text = re.sub(r"[^a-zA-Z0-9À-ÿ\s]", "", text)  # Enlever caractères spéciaux
    return text.strip()

cleaned_lines = [clean_text(line) for line in selected_lines if len(line.split()) > 3]  # Supprime les phrases trop courtes

# 🔹 Étape 4 : Sauvegarder le texte nettoyé
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_lines))

print(f"✅ Extraction et nettoyage terminés ! Résultat : {output_file}")
