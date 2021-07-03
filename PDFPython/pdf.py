import PyPDF2
import sys

inputs = sys.argv[1:] #ia toate argumentele intr o lista inputs[]


with open('dummy.pdf', 'rb') as file:    #rb e standard; rb = read binary;
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)
	print(reader.getPage(0))
	page = reader.getPage(0)    #asta imi ia prima pagina ;
	print(page.rotateCounterClockwise(90))  #roteste la 90 de grade , dar e doar in memorie;
	writer = PyPDF2.PdfFileWriter() 
	writer.addPage(page)
	with open("tilt.pdf", "wb") as new_file:
		writer.write(new_file)
    



