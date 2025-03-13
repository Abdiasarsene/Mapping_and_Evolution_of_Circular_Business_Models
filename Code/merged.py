import os
import glob

# 🔹 Dossier contenant les fichiers .txt
input_folder = r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models"  
output_file = r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\Text_data.txt"  # ✅ Ajouter .txt

# 🔹 Ouvrir le fichier de sortie en mode écriture
with open(output_file, "w", encoding="utf-8") as outfile:
    for file_path in glob.glob(os.path.join(input_folder, "*.txt")):
        with open(file_path, "r", encoding="utf-8") as infile:
            outfile.write(f"\n### Contenu de {os.path.basename(file_path)} ###\n\n")  # Ajout du nom du fichier
            outfile.write(infile.read() + "\n")  # Ajouter le contenu du fichier
        print(f"✅ {file_path} ajouté au fichier fusionné.")

print(f"\n🎯 Fusion terminée ! Le fichier final est : {output_file}")
