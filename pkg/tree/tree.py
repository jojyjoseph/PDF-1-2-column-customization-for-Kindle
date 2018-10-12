import logging
from pkg.helper.helper import *

try:
    from pkg.tree import bookIndexTree
    from pkg.tree import splitPageIndexTree
    from pkg.tree import pageSizeIndexTree
    from pkg.helper import gv
except ImportError:
    log_error("ImportError : pkg/tree/tree.py")




class Tree:

    #constructor
    def __init__(self):
        self.m_BookIndex        = bookIndexTree.BookIndexTree(str(gv.BookIndexPath))
        self.m_SplitPageIndex   = splitPageIndexTree.SplitPageIndexTree(str(gv.SplitPageDetailPath))
        self.m_PageSizeIndex    = pageSizeIndexTree.PageSizeIndexTree(str(gv.PageSizePath))

# functions in BookIndexTree
    def getChapterList(self):
        return self.m_BookIndex.getChapterList()

    def getStartPage(self):
        return self.m_BookIndex.getStartPage()


#functions in SplitPageIndexTree
    def getPagesBeforeSplit(self):
        return self.m_SplitPageIndex.getPagesBeforeSplit()

    def getPagesAfterSplit(self):
        return self.m_SplitPageIndex.getPagesAfterSplit()

#functions in pageSizeIndexTree
    def getTop(self,layout):
        return self.m_PageSizeIndex.getTop(layout)

    def getBottom(self,layout):
        return self.m_PageSizeIndex.getBottom(layout)

    def getLeft(self,layout):
        return self.m_PageSizeIndex.getLeft(layout)

    def getRight(self,layout):
        return self.m_PageSizeIndex.getRight(layout)

