import pandas as pd
from docx import Document

document = Document('H:/Lessons/The Power of Silence.docx')
text = []
for paragraph in document.paragraphs:
    text.append(paragraph.text)


data = pd.DataFrame(text, columns=['Text'])
print(text)