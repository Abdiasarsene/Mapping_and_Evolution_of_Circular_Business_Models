# Importing librairy 
import pandas as pd
import spacy

economic = pd.read_csv(r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\economic.txt", delimiter="\t", encoding="utf-8")

# Initializing spacy
nlp = spacy.load("en_core_web_sm")
def number_proper_noun(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_digit and token.pos_ != "PROPN"]
    return " ".join(tokens)

economic["Text_cleans_propn"] = economic["Text_cleaned"].astype(str).apply(number_proper_noun)