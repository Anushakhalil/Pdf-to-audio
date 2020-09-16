import pyttsx3
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def pdf_to_text(path):
    output_string = StringIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmngr = PDFResourceManager()
        device = TextConverter(rsrcmngr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmngr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    text = output_string.getvalue()
    C = text
    L = list(C.split('\n'))
    for i, v in enumerate(L):
        if "| P a g e" in v or "P a g e |" in v or "Page" in v:
            L.remove(v)

    new_text = "\n".join(L)
    print(new_text)
    SpeakText(new_text)


def SpeakText(command):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 30)
    engine.save_to_file(command, filename="test.mp3")
    engine.runAndWait()


print("Enter the path to the file ")
path=input("Enter: ")
pdf_to_text(path)
