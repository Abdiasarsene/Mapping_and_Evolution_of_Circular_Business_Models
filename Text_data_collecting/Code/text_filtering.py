import os
import glob

# Liste des mots-clés pour le filtrage (ajoutez vos synonymes ici)
keywords_dict = {
    "Circular Economy": ["circular economy", "reuse", "recycling", "repair", "closed loops", "sustainability", "R strategies"],
    "Circular Business Models": ["circular business models", "Product-as-a-Service", "PaaS", "lifecycle extension", "refurbishment", "remanufacturing", "industrial symbiosis", "circular supply chains"],
    "Business Model Archetypes": ["archetypes", "circular strategies", "value creation", "organizational innovation", "diversification"],
    "Technology and Innovation": ["Internet of Things", "IoT", "blockchain", "additive manufacturing", "3D printing", "sensors", "material flow optimization"],
    "Sustainability": ["ecological", "economic", "social sustainability", "environmental impact", "sustainable value creation"],
    "Regulation and Policies": ["Extended Producer Responsibility", "EPR", "circular regulations", "Circular Economy Action Plan", "financial incentives"],
    "Management and Organizational Strategies": ["organizational adoption", "change management", "supply chain collaboration", "industrial network cooperation"],
    "Literature Trends and Development": ["societal transitions", "emerging trends", "development patterns", "implementation challenges"]
}

# Dossier contenant les fichiers .txt
input_folder = r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\Python_code"
output_folder = r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\Text_data"

# Vérifier si le dossier de sortie existe, sinon le créer
os.makedirs(output_folder, exist_ok=True)

# Parcourir tous les fichiers .txt dans le dossier
for file_path in glob.glob(os.path.join(input_folder, "*.txt")):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Filtrer les lignes contenant un mot-clé
    filtered_lines = [line for line in lines if any(keyword.lower() in line.lower() for keyword in keywords_dict)]

    # Sauvegarder les résultats dans un nouveau fichier
    if filtered_lines:
        output_path = os.path.join(output_folder, os.path.basename(file_path))
        with open(output_path, "w", encoding="utf-8") as f_out:
            f_out.writelines(filtered_lines)
        print(f"✅ Fichier filtré : {output_path}")

print("🎯 Filtrage terminé pour tous les fichiers !")
