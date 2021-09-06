from gtts import gTTS
import PyPDF2
import sys

input = open(sys.argv[1], 'rb')
pdfReader = PyPDF2.PdfFileReader(input)
totalPages = pdfReader.numPages

text = ""

pageNum = 0
while pageNum < totalPages:
    page = pdfReader.getPage(pageNum)
    text += page.extractText()
    print('extracted text from page',  pageNum)
    pageNum+=1

input.close()

tts = gTTS(text)
tts.save(sys.argv[2])
