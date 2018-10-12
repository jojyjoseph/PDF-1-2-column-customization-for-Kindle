import logging
from pkg.helper.helper import *

try:
    from pkg.helper import gv
    from pkg.tree import tree
    from pkg.book import page
except ImportError:
    log_error("ImportError : pkg/book/chapter.py")




class Chapter:
    newbookpagenumber  =1
    oddeven=1
        
    #constructor
    def __init__(self,chapter_arg,tree_arg):
        self.pages= []
        self.tree=tree_arg
        self.chapter=chapter_arg
        self.pageiter=int((self.chapter)[2])
        self.createPages()

    def createPages(self):
        self.createPagesBeforeSplit()
        self.createPagesDuringSplit()
        self.createPagesAfterSplit()


    def createPagesBeforeSplit(self):
        for i in range(self.tree.getPagesBeforeSplit()):
            log_info("Processing parent page - {}".format(self.pageiter))
            p=self.makeFullPage(self.pageiter)
            self.incrementPageIter()

    def createPagesDuringSplit(self):
        pages=(int(self.chapter[3]) -int(self.chapter[2]) +1) - self.tree.getPagesBeforeSplit()  - self.tree.getPagesAfterSplit()
        for i in range(pages):
            log_info("Processing parent page - {}".format(self.pageiter))
            self.makeSplitPage(self.pageiter)
            self.incrementPageIter()

    def createPagesAfterSplit(self):
        for i in range(self.tree.getPagesAfterSplit()):
            log_info("Processing parent page - {}".format(self.pageiter))
            p=self.makeFullPage(self.pageiter)
            self.incrementPageIter()

    def makeFullPage(self,pagenumber):
        
        if ((pagenumber%2) == Chapter.oddeven): # assuming even is on right side
            layout = page.Layout.FullPageRight
        else:
            layout = page.Layout.FullPageLeft

        p = page.Page(pagenumber, self.getNewBookPageNumber(), layout)
        log_info("Processing new book page - {}".format(p))

        self.pages.append(p)

        self.incrementNewBookPageNumber()



    def makeSplitPage(self,pagenumber):
        if ((pagenumber%2) == Chapter.oddeven):
            layout11 = page.Layout.RightPageLeftSideTop
            layout12 = page.Layout.RightPageLeftSideBottom
            layout21 = page.Layout.RightPageRightSideTop
            layout22 = page.Layout.RightPageRightSideBottom
        else:
            layout11 = page.Layout.LeftPageLeftSideTop
            layout12 = page.Layout.LeftPageLeftSideBottom
            layout21 = page.Layout.LeftPageRightSideTop
            layout22 = page.Layout.LeftPageRightSideBottom


        p11 = page.Page(pagenumber,self.getNewBookPageNumber(), layout11)
        log_info("Processing new book page - {}".format(p11))
        self.incrementNewBookPageNumber()
        p12 = page.Page(pagenumber,self.getNewBookPageNumber(), layout12)
        log_info("Processing new book page - {}".format(p12))
        self.incrementNewBookPageNumber()
        p21 = page.Page(pagenumber,self.getNewBookPageNumber(), layout21)
        log_info("Processing new book page - {}".format(p21))
        self.incrementNewBookPageNumber()
        p22 = page.Page(pagenumber,self.getNewBookPageNumber(), layout22)
        log_info("Processing new book page - {}".format(p22))
        self.incrementNewBookPageNumber()
        self.pages.extend((p11,p12,p21,p22))


    def incrementPageIter(self):
        self.pageiter = self.pageiter + 1

    def incrementNewBookPageNumber(self):
        Chapter.newbookpagenumber = Chapter.newbookpagenumber + 1

    def getNewBookPageNumber(self):
        return int(Chapter.newbookpagenumber)
    
    def getChapterNewPages(self):
        return self.pages
