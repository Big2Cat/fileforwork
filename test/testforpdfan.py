#!/usr/bin/env python
# encoding: utf-8

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
pdf_content = open('~/Desktop/fxrjxyl.pdf','rb')
parser = PDFParser(pdf_content)
document = PDFDocument(parser)

outlines = document.get_outlines()
for (level, title, dest,a,se) in outlines:
    print (level,title)
