# Importing librairy
import fitz

# PDF PATH
pdf_path = r"C:\Users\HP ELITEBOOK 840 G6\Downloads\final.pdf"

doc = fitz.open(pdf_path)

text = ""
for page in doc:
    text += page.get_text("text") + "\n"
doc.close()

# Export text data
with open("ext1.txt", "w", encoding="utf-8") as f : 
    f.write(text)

