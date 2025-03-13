# Importing librairies
import pandas as pd
from langdetect import detect

# Importing text data
langue = pd.read_excel(r'D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\text_data.xlsx')

# Removing other languages funtion
def remove_non_english(text):
    try:
        return text if detect(text) == "en" else ""
    except:
        return ""

langue['Text_non_english'] = langue['Text_cleans_propn'].astype(str).apply(remove_non_english)