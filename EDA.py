# Importing of librairy
import pandas as pd 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy
import gensim
from gensim import corpora
import pyLDAvis.gensim_models as gensimvis
import pyLDAvis

# Importing text data 
circular = pd.read_csv(r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\Text_data\circular_economic.csv")

# Removal a subtle columns
circular.drop(columns=['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6'])

texte = " ".join(circular['Text_non_english'].dropna().astype(str))
# WordCloud
wordcloud = WordCloud(height=400, width=800, background_color='white',colormap='coolwarm').generate(texte)

# Graphical visualization
plt.figure(figsize=(12, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.title("WordCloud ot text data")
plt.show()

# Importation des bibliothèques
import pandas as pd
import spacy
import gensim
from gensim import corpora
import pyLDAvis.gensim_models as gensimvis
import pyLDAvis

# Charger les données
circular = pd.read_csv(r"D:\Projects\IT\Data Science & IA\Mapping_Evolution_of_Circular_Business_Models\Text_data\circular_economic.csv")

# Supprimer les valeurs NaN et convertir en texte
circular = circular.dropna(subset=['Text_non_english'])
circular['Text_non_english'] = circular['Text_non_english'].astype(str)

# Charger SpaCy avec un modèle moyen (recommandé pour une meilleure précision)
nlp = spacy.load("en_core_web_md")

# Prétraitement : Tokenisation + Lemmatisation
def preprocess_text(text):
    doc = nlp(text.lower())  # Mettre en minuscule et tokeniser
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]  # Lemmatisation + suppression des stopwords

# Appliquer le prétraitement
circular['processed_text'] = circular['Text_non_english'].apply(preprocess_text)

# Création du dictionnaire et du corpus
dictionary = corpora.Dictionary(circular['processed_text'])
corpus = [dictionary.doc2bow(text) for text in circular['processed_text']]

# Modèle LDA - Extraction de thèmes (5 thèmes, 10 passes)
lda_model = gensim.models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)

# Visualisation des thèmes avec pyLDAvis
lda_vis = gensimvis.prepare(lda_model, corpus, dictionary)
pyLDAvis.show(lda_vis)
