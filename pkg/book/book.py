import logging
from pkg.helper.helper import *

try:
    from pkg.helper import gv
    from pkg.tree import tree
    from pkg.book import chapter
    from pkg.pdf import pdfpkg
except ImportError:
    log_error("ImportError : pkg/book/book.py")




class Book:

    #constructor
    def __init__(self):
        self.chapters = []
        self.t=tree.Tree()

        #for chapter in chapter list
        for ch in self.t.getChapterList():
            c=chapter.Chapter(ch,self.t)
            self.chapters.append(c)

    def getBookChapters(self):
        return self.chapters
    
    def bookPrint(self):
        log_info("Printing of book starting")
        pdf=pdfpkg.PdfPkg()
        
        for ch in self.getBookChapters():
            for page in ch.getChapterNewPages():
                page.pageprint(pdf,self.t)

        log_info("writing to pdf file")
        with open("out.pdf",'wb') as out:
            pdf.pdfwriter.write(out)



