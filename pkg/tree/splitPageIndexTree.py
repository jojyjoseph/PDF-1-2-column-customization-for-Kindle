import logging
from pkg.helper.helper import *

try:
    import xml.etree.ElementTree as ET
except ImportError:
    log_error("ImportError : pkg/book/splitPageIndexTree.py")



class SplitPageIndexTree:
    
    #Constructor
    def __init__(self,path):
        self.splitPageIndexTree = ET.parse(path)
        log_info("Parsing xml file : " + str(path))
        self.splitPageIndexTreeRoot = self.splitPageIndexTree.getroot()
        self.splitpagebegin = int(self.splitPageIndexTreeRoot.find('splitpagebegin').text)
        self.splitpageend   = int(self.splitPageIndexTreeRoot.find('splitpageend').text)

    def getPagesBeforeSplit(self):
        return (self.splitpagebegin)

    def getPagesAfterSplit(self):
        return self.splitpageend

