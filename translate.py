
import PyPDF2 

pdfFileObj = open('example.pdf', 'rb') 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

strings = ""
for i in range(pdfReader.numPages):
	strings += pdfReader.getPage(i).extractText()

print(strings) 
 
pdfFileObj.close() 

######################################### for translating ##################
from googletrans import Translator

translator = Translator()

translated_sentence = translator.translate(strings, src='en', dest='ja')

print(translated_sentence.text)

####################to pdf##############

from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.add_font('fireflysung', '', 'font/fireflysung.ttf', uni=True)
pdf.set_font('fireflysung', '', 14)
pdf.write(8, translated_sentence.text)
pdf.ln(15)

pdf.output("unicode.pdf", 'F')