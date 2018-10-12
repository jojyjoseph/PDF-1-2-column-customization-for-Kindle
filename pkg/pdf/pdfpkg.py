import logging
from pkg.helper.helper import *

try:
    from pkg.helper import gv
    from PyPDF2 import PdfFileWriter, PdfFileReader
except ImportError:
    log_error("ImportError : pkg/pdf/pdfpkg.py")




class PdfPkg:

    #constructor
    def __init__(self):
        #self.m_BookIndex = bookIndexTree.BookIndexTree(str(gv.BookIndexPath))
        #self.m_SplitPageIndex = splitPageIndexTree.SplitPageIndexTree(str(gv.SplitPageDetailPath))
        self.pdfread = None
        f_read=open(gv.inputpdffile,'rb')
        if f_read:
            self.pdfread=PdfFileReader(f_read)
        else:
            return

        self.pdfread1 = None
        f_read=open(gv.inputpdffile1,'rb')
        if f_read:
            self.pdfread1=PdfFileReader(f_read)
        else:
            return

        self.pdfread2 = None
        f_read=open(gv.inputpdffile2,'rb')
        if f_read:
            self.pdfread2=PdfFileReader(f_read)
        else:
            return

        self.pdfread3 = None
        f_read=open(gv.inputpdffile3,'rb')
        if f_read:
            self.pdfread3=PdfFileReader(f_read)
        else:
            return

        self.pdfread4 = None
        f_read=open(gv.inputpdffile4,'rb')
        if f_read:
            self.pdfread4=PdfFileReader(f_read)
        else:
            return

 
   
        self.pdfwriter=PdfFileWriter()

        #leftLeft
        #p=self.pdfread.getPage(1)
        #p.cropBox.lowerLeft=(115,250)
        #p.cropBox.upperRight=(300,700)
        #leftright
        #p=self.pdfread.getPage(1)
        #p.cropBox.lowerLeft=(295,250)
        #p.cropBox.upperRight=(480,700)
        #RightLeft
        #p=self.pdfread.getPage(4)
        #p.cropBox.lowerLeft=(125,250)
        #p.cropBox.upperRight=(310,700)
        #righright
        #p=self.pdfread.getPage(4)
        #p.cropBox.lowerLeft=(310,250)
        #p.cropBox.upperRight=(495,700)
        
        #p=self.pdfread.getPage(1)
        #self.pdfwriter.addPage(p)
        #with open("out.pdf",'wb') as out:
         #   self.pdfwriter.write(out)





