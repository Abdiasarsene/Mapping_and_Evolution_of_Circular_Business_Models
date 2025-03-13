# Importing librairies
import fitz

pdf = r"C:\Users\HP ELITEBOOK 840 G6\Downloads\FullConferenceProceedings_NBM2019.pdf"

doc = fitz.open(pdf)

# Extract text data
text =""

for page in doc :
    text += page.get_text("text") + "\n"

doc.close()

with open('text_extraction.txt', "w", encoding="utf-8") as f:
    f.write(text)