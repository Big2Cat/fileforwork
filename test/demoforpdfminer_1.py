#!/usr/bin/env python
# encoding: utf-8

import os
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

#将一个pdf转换成txt
def pdfTotxt(filepath,outpath):
    try:
        fp = file(filepath, 'rb')
        outfp=file(outpath,'w')
        #创建一个PDF资源管理器对象来存储共享资源
        #caching = False不缓存
        rsrcmgr = PDFResourceManager(caching = False)
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = TextConverter(rsrcmgr, outfp, codec='utf-8', laparams=laparams,imagewriter=None)
        #创建一个PDF解析器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, pagenos = set(),maxpages=0,
                                      password='',caching=False, check_extractable=True):
            page.rotate = page.rotate % 360
            interpreter.process_page(page)
        #关闭输入流
        fp.close()
        #关闭输出流
        device.close()
        outfp.flush()
        outfp.close()
    except Exception, e:
         print "Exception:%s",e

def doWithtxt(outpath):

    issuerspattern = re.compile(u'发行人：(.*)')
    bondsnamepattern = re.compile(u'债券名称：(.*\n*.*)。')
    bondscompanypattern = re.compile(u'担保人基本情况.*\n*.*公司名称：(.*)')
    corporatepattern = re.compile(u'发行人概况.*(\s|\S)*?法定代表人：(.*)')
    companytypepattern = re.compile(u'发行人概况.*(\s|\S)*?企业类型：(.*)')
    try:
        txtcontent = open(outpath,'r').read().decode('utf-8')
        #解析出来的债券名称
        bondsname = re.sub('\n','',re.search(bondsnamepattern,txtcontent).group(1))
        #解析出来的发行人
        issuers = re.search(issuerspattern,txtcontent).group(1)
        #担保人（担保公司）
        bondscompany = re.search(bondscompanypattern,txtcontent).group(1)
        #法定代表人
        corporate = re.search(corporatepattern,txtcontent).group(2)
        #发行人企业类型
        companytype = re.search(companytypepattern,txtcontent).group(2)

    except Exception as e:

        print e

pdfTotxt('/home/kong/Desktop/fxrjxyl.pdf','test.txt')

#一个文件夹下的所有pdf文档转换成txt
def pdfTotxtA(fileDir):
    files=os.listdir(fileDir)
    tarDir=fileDir+'txt'
    if not os.path.exists(tarDir):
        os.mkdir(tarDir)
    replace=re.compile(r'\.pdf',re.I)
    for file in files:
        filePath=fileDir+'\\'+file
        outPath=tarDir+'\\'+re.sub(replace,'',file)+'.txt'
        pdfTotxt(filePath,outPath)
        print "Saved "+outPath

#pdfTotxtA(u'F:\\pdf\\2013')
