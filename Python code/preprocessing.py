# Importing librairy
import pandas as pd
import spacy

# Importing text data
text_data = pd.read_csv(r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\filtered_text.txt", delimiter='\t', encoding="utf-8", names=["Text"])

data_text = text_data.rename(columns={"Phrase": 'Results of providing feedback information in a field trial No S62011 Working paper sustainability'})

# Preprocessing with spacy
nlp = spacy.load("en_core_web_sm")

# Define stop word
custom_stop_word = {
    "i", "you", "he", "she", "we", "they", "it", "my", "your", "his", "her", "our", "their",
    "me", "him", "us", "them", "is", "are", "was", "were", "be", "been", "being", 
    "a", "an", "the", "this", "that", "these", "those", "and", "but", "or", "if", "because", "so",
    "on", "in", "at", "by", "with", "about", "against", "between", "into", "through", "over", "under",
    "again", "further", "then", "once", "can", "will", "just", "should", "would", "could", "may", "might", "must","include", "mention", "already", "quickly", "soon", "allow", "out", "second", "far",
    "market", "million", "stock", "general", "industry", "economy", "nation", "education",
    "moment", "parent", ""
}

nlp.Defaults.stop_words.update(custom_stop_word)
# Pretreatment function
def preprocesing(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and token.lemma_ not in custom_stop_word]
    return " ".join(tokens)

data_text['Text_cleaned'] = data_text['Phrase'].astype(str).apply(preprocesing)

data_text['Text_cleaned']

economic = pd.read_csv(r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\economic.txt", delimiter="\t", encoding="utf-8")

def number_proper_noun(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_digit and token.pos_ != "PROPN"]
    return " ".join(tokens)

economic["Text_cleans_propn"] = economic["Text_cleaned"].astype(str).apply(number_proper_noun)