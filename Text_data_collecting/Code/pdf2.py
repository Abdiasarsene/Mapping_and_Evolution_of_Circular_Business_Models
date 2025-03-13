# Importing librairy
import fitz

# Pdf path
pdf_text = r"C:\Users\HP ELITEBOOK 840 G6\Downloads\NBM2022_BOP_FINAL.pdf"

doc = fitz.open(pdf_text)
text =""
for page in doc:
    text += page.get_text("text") + "\n"

doc.close()

# Export text data 
with open("text2.txt","w",encoding="utf-8") as f:
    f.write(text)