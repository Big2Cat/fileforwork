#!/usr/bin/python
#-*- coding: utf-8 -*-

from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import *
import re
import json

#打开一个pdf文件
fp = open('/home/kong/Desktop/fxrjxyl.pdf', 'rb')
#创建一个PDF文档解析器对象
parser = PDFParser(fp)
#创建一个PDF文档对象存储文档结构
#提供密码初始化，没有就不用传该参数
#document = PDFDocument(parser, password)
document = PDFDocument(parser)
#检查文件是否允许文本提取
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
#创建一个PDF资源管理器对象来存储共享资源
#caching = False不缓存
rsrcmgr = PDFResourceManager(caching = False)
# 创建一个PDF设备对象
laparams = LAParams()
# 创建一个PDF页面聚合对象
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#创建一个PDF解析器对象
interpreter = PDFPageInterpreter(rsrcmgr, device)
#处理文档当中的每个页面

# doc.get_pages() 获取page列表
#for i, page in enumerate(document.get_pages()):
#PDFPage.create_pages(document) 获取page列表的另一种方式
replace=re.compile(r'\s+');
#re.search(u'中文.*(\s|\S)*。',to_re.decode('utf-8'),re.M).group(0)
bondspattern = re.compile(u'债券名称：.*债券')
issurespattern = re.compile(u'发行人：.+(\s|\S)*。')
credit_improve_compattern = re.compile(u'债券担保：(.*)\。',re.DOTALL)
# 循环遍历列表，每次处理一个page的内容
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    # 接受该页面的LTPage对象
    layout=device.get_result()
    # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
    # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
    for x in layout:
        if(isinstance(x,LTTextBox)):
            #print x.get_text()
    #for x in layout:
        #如果x是水平文本对象的话
        #if(isinstance(x,LTTextBoxHorizontal)):
            #re_d = re.sub('\n\n','',x.get_text())
            #print re_d'''
            try:
                #cre_imp_com = re.search(credit_improve_compattern,x.get_text()).group()
                #issures = re.search(issurespattern,x.get_text()).group()
                bonds_name = re.search(u'债券名称：.*(\n)*.*。',x.get_text()).group()
                #print issures
                print bonds_name
                #print cre_imp_com
            except:
                pass
            #text=re.sub(replace,'',x.get_text())
            #issures = re.search('(发行人)',text).group(1)
            #print '发行人是:{issures}'.format(issures=issure)
