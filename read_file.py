# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

#pip list | grep -F docx
from werkzeug.datastructures import FileStorage		#pip install werkzeug
import PyPDF2										#pip install PyPDF2
import tempfile
from PIL import Image								#pip install Pillow
#import pytesseract									#pip install pytesseract
from pdf2image import convert_from_path				#pip install pdf2image
import docx											#pip install docx  pip install python-docx

class ReadFile():

	def text_pdf(f, directory):
		text = ""
		pdfFileObj = open(directory + f.filename, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		for page_number in range(pdfReader.getNumPages()):
			pageObj = pdfReader.getPage(page_number)
			text += pageObj.extractText()
		return text
					
# 	def image_pdf(f, directory):
# 		text = ""
# 		pages = convert_from_path(directory + f.filename, 500)
# 		image_counter = 1
# 		for page in pages:
# 			filename = "page_"+str(image_counter)+".jpg"
# 			page.save(directory + filename, 'JPEG')
# 			image_counter = image_counter + 1
# 		filelimit = image_counter-1
# 		for i in range(1, filelimit + 1):
# 			filename = "page_"+str(i)+".jpg"
# 			pagetext = str(((pytesseract.image_to_string(Image.open(directory + filename)))))
# 			pagetext = pagetext.replace('-\n', '') 
# 			text += pagetext 
# 		return text
	
	def docx_file(f, directory):										#does not work for tables, headers, footers, foot notes
		text = ""
		doc = docx.Document(directory + f.filename)
		for para in doc.paragraphs:
			text += para.text
		return text
	
	def txt_file(f, directory):
		f = open(directory + f.filename, "r")
		text = f.read()
		return text

	def read_func(f):
		print("Enter: read_file.py")
		print(type(f)) 													#FileStorage
		print(f.filename)
		print(f.filename.split('.')[1])
		print(f.content_type)
		text = "Error: unable to read file"
		
		with tempfile.TemporaryDirectory() as directory:				#creates a temp directory and then deletes 
			f.save(directory + f.filename)
			
			if (f.filename.split('.')[1] == "txt"):
				text = ReadFile.txt_file(f, directory)
		
			elif (f.filename.split('.')[1] == "docx"): 
				text = ReadFile.docx_file(f, directory)
			
			elif (f.filename.split('.')[1] == "pdf"): 
				text = ReadFile.text_pdf(f, directory) 						#text PDFs
# 				if (text == ""): 
# 					text = ReadFile.image_pdf(f, directory) 				#image PDFs
					
		print("Exit: read_file.py")
		return text
		
		
