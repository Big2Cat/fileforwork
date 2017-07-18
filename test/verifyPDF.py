#!/usr/bin/env python
# encoding: utf-8

from __future__ import division
import os
from PyPDF2 import PdfFileReader

def pdf_verify(filepath):


    listDir = os.listdir(filepath)
    allPdf = len(listDir)
    count = 0
    for pdfFile in listDir:

        FileObj = open(filepath+pdfFile,'rb')

        PdfObj = PdfFileReader(FileObj)

        if PdfObj.isEncrypted:

            count += 1

    print '文件总的份数是:%d'%allPdf
    print '加密的份数是:%d'%count
    print '加密的份数所占的比例为'+str(count/allPdf)


pdf_verify('/home/kongspider/spiderDir/PDFfiles')
