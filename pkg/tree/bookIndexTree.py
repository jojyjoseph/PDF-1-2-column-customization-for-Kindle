import logging
from pkg.helper.helper import *

try:
    import xml.etree.ElementTree as ET
except ImportError:
    log_error("ImportError : pkg/tree/bookIndexTree.py")



class BookIndexTree:
    
    #Constructor
    def __init__(self,path):
        self.booktree = ET.parse(path)
        log_info("Parsing xml file : " + str(path))
        
        self.book = self.booktree.getroot()
        self.chaptersTree=self.book.find('Chapters')
        self.bookStartPage=int(self.book.find('startpage').text)
        self.bookEndPage = int(self.book.find('endpage').text)

    def check(self):
        log_test("check")

    def getChapterList(self):
        self.chapterList=[]
        
        for ch in self.chaptersTree.findall('Chapter'):
            if not ch:
                print("no ch")
            else:
                number=int(ch.find('Chapterno').text)
                name=str(ch.find('Name').text).strip()
                startpage=int(ch.find('startpage').text)
                lastpage= self.bookEndPage
                for ch_next in self.chaptersTree.findall('Chapter'):
                    if(int(ch_next.find('Chapterno').text) ==  (number+1)):
                        lastpage = int(ch_next.find('startpage').text) - 1
                self.chapterList.append((number,name,startpage,lastpage))

        return self.chapterList

    def getStartPage(self):
        return self.bookStartPage

