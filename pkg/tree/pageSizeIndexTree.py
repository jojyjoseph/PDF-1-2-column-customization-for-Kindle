import logging
from pkg.helper.helper import *

try:
    import xml.etree.ElementTree as ET
except ImportError:
    log_error("ImportError : pkg/tree/pageSizeTree.py")



class PageSizeIndexTree:
    
    #Constructor
    def __init__(self,path):
        self.pagesizetree=ET.parse(path)
        self.pagesizeroot=self.pagesizetree.getroot()

    def getTop(self,layouttype_arg):
        layouttype=str(layouttype_arg)
        log_test("Check value : {}".format(layouttype))
        pagesizetype=self.pagesizeroot.find('pagesizetypes')
        for type in pagesizetype.findall('type'):
            if type.get('name')==layouttype:
                return int(type.find('top').text)

    def getBottom(self,layouttype_arg):
        layouttype=str(layouttype_arg)
        log_test("Check value : {}".format(layouttype))
        pagesizetype=self.pagesizeroot.find('pagesizetypes')
        for type in pagesizetype.findall('type'):
            if type.get('name')==layouttype:
                return int(type.find('bottom').text)

    def getRight(self,layouttype_arg):
        layouttype=str(layouttype_arg)
        log_test("Check value : {}".format(layouttype))
        pagesizetype=self.pagesizeroot.find('pagesizetypes')
        for type in pagesizetype.findall('type'):
            if type.get('name')==layouttype:
                return int(type.find('right').text)

    def getLeft(self,layouttype_arg):
        layouttype=str(layouttype_arg)
        log_test("Check value : {}".format(layouttype))
        pagesizetype=self.pagesizeroot.find('pagesizetypes')
        for type in pagesizetype.findall('type'):
            if type.get('name')==layouttype:
                return int(type.find('left').text)



