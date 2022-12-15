#file Reader by URL Program 

#importing urllib for process url func
from urllib import request as ur
#need to install PyPDf2 lib to access pdf files
import PyPDF2.PdfFileReader as pdfr
url=input("enter url")
file=ur.urlopen(url)
if url[-3:].lower()=="pdf":
    file=pdfr(url)
for line in file:
    #decode the file to read the data
    a=line.decode('utf-8').strip()
    print(a)
