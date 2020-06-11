import PyPDF2
from PIL import Image
##import matplotlib.pyplot as plt
import time
import camelot
import pandas as pd
import csv
import textract
pdf=open('bvp stand alone.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdf)
numpages=pdfReader.getNumPages()

if pdfReader.isEncrypted:
    pdfReader.decrypt('')
##text=textract.process("bvp stand alone.pdf",method='pdfminer')
##print(text)
for i in range(numpages):
    pageObj=pdfReader.getPage(i)
    k=pageObj.extractText()
    print("Page number ",i+1)
##    print(k.split()) #it is less readable
    print(k)
    print("\n")



##for j in range(numpages):
    page0= pdfReader.getPage(2)
    xObject = page0['/Resources']['/XObject'].getObject()
    page2= pdfReader.getPage(5)
    for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                    data = xObject[obj].getData()
                    if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                        mode = "RGB"
                    else:
                        mode = "P"

                    if xObject[obj]['/Filter'] == '/FlateDecode':
                        img = Image.frombytes(mode, size, data)
                        img.save(obj[1:] + ".png")
                    elif xObject[obj]['/Filter'] == '/DCTDecode':
                        img = open(obj[1:] + ".jpg", "wb")
                        img.write(data)
                        img.close()
                    elif xObject[obj]['/Filter'] == '/JPXDecode':
                        img = open(obj[1:] + ".jp2", "wb")
                        img.write(data)
                        img.close
                                     
img.show()

tables=camelot.read_pdf('bvp stand alone.pdf',pages="1-end")
print(tables[5].df)
tables[4].to_csv("table.csv")

##Trying to remove whitespaces from csv

##df=pd.read_csv("table.csv",delimiter=" ")
##reader =csv.DictReader(open('table.csv'),skipinitialspace=True)
###next(reader)
##names=reader.fieldnames
##for row in reader:
##  for f in names:
##      row[f]=row[f].strip()
##print(row)
      



