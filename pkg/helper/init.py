import logging
from pkg.helper.helper import *

try:
    import shutil
    import os
except ImportError:
    log_error("ImportError : pkg/helper/init.py")
    

def dellogfile():
    if os.path.exists('./logfile'):
        os.remove('./logfile')

def logfileinit():
    dellogfile()
    logging.basicConfig(filename='logfile', level=logging.DEBUG)

def del4PDF():
    if os.path.exists('in1.pdf'):
        os.remove('in1.pdf')
    if os.path.exists('in2.pdf'):
        os.remove('in2.pdf')
    if os.path.exists('in3.pdf'):
        os.remove('in3.pdf')
    if os.path.exists('in4.pdf'):
        os.remove('in4.pdf')

def copyPDF4():
    
    del4PDF()
    
    shutil.copyfile('in.pdf','in1.pdf')
    shutil.copyfile('in.pdf','in2.pdf')
    shutil.copyfile('in.pdf','in3.pdf')
    shutil.copyfile('in.pdf','in4.pdf')

def init():
    logfileinit()
    copyPDF4()

def deinit():
    del4PDF()

__all__=['init','deinit']

