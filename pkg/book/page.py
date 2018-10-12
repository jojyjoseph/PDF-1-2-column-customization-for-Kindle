import logging
from pkg.helper.helper import *

try:
    from pkg.helper import gv
    from pkg.tree import tree
    from enum import Enum
    import re
    from PyPDF2 import PdfFileWriter, PdfFileReader
except ImportError:
    log_error("ImportError : pkg/book/page.py")


class Layout(Enum):
    FullPageNormal              = 1
    FullPageLeft                = 2
    FullPageRight               = 3
    LeftPageLeftSideTop         = 4
    LeftPageLeftSideBottom      = 5
    LeftPageRightSideTop        = 6
    LeftPageRightSideBottom     = 7
    RightPageLeftSideTop        = 8
    RightPageLeftSideBottom     = 9
    RightPageRightSideTop       = 10
    RightPageRightSideBottom    = 11



class Page:

    def __init__(self, parentpagenumber, newbookpagenumber, layoutdetails):
        self.parentpagenumber   = parentpagenumber
        self.newbookpagenumber  = newbookpagenumber
        self.layoutdetails      = layoutdetails

    def __str__(self):
        return "Parentpage %s, NewBookPageNumber %s, Layoutdetails %s" %(self.parentpagenumber, self.newbookpagenumber, repr(self.layoutdetails))
    
    def pageprint(self,pdf,tree):
        log_info("processing page for pdf : {}".format(self.__str__()))
        layout=self.trimLayoutEnum(self.layoutdetails)
        log_info("layout value : {}".format(layout))

        if (layout=='RightPageLeftSideTop') or (layout=='LeftPageLeftSideTop'):
            inpdf=pdf.pdfread1
        elif (layout=='RightPageLeftSideBottom') or (layout=='LeftPageLeftSideBottom'):
            inpdf=pdf.pdfread2
        elif (layout=='RightPageRightSideTop') or (layout=='LeftPageRightSideTop'):
            inpdf=pdf.pdfread3
        elif (layout=='RightPageRightSideBottom') or (layout=='LeftPageRightSideBottom'):
            inpdf=pdf.pdfread4
        else:
            inpdf=pdf.pdfread
        self.page=inpdf.getPage(self.parentpagenumber -tree.getStartPage())
        
        
         #page.cropBox.lowerLeft(tree.getLeft(layout),tree.getBottom(layout))
        #page.cropBox.upperRight(tree.getRight(layout),tree.getTop(layout))
        left    =tree.getLeft(layout)
        bottom  =tree.getBottom(layout)
        right   =tree.getRight(layout)
        top     =tree.getTop(layout)
        log_info("Layout dimension - left :  {} , right : {} , top : {} , bottom : {}".format(left,right,top,bottom))
        self.page.cropBox.lowerLeft=(left,bottom)
        self.page.cropBox.upperRight=(right,top)
        log_info("Page info {}".format(self))
        pdf.pdfwriter.addPage(self.page)
        #self.printIndividualPage() #enable this to print individual page
       

    def trimLayoutEnum(self,layoutstr):
        return str(re.sub("Layout.","",str(layoutstr)))


    def printIndividualPage(self):
        writer=PdfFileWriter()
        writer.addPage(self.page)
        with open("page"+str(self.newbookpagenumber),'wb') as out:
            writer.write(out)
__all__ = ['Page', 'Layout']
