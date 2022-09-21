import PyPDF2
from gtts import gTTS 
import os 

def handle_uploaded_file(f, n, ex):
    with open(f'static/media/pdf_local/{n}.{ex}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return f


def pdfReader(file):
    f = open(file, "rb") 
    reader=PyPDF2.PdfFileReader(f)
    # print(reader.numPages)
    page1=reader.getPage(0)
    pdfText = page1.extractText()
    return pdfText


def text_to_audio(text, path, lang):
    objet = gTTS(text=text, lang=lang, slow=False)
    test = objet.save(path)
    return path
