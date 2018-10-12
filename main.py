import logging
from pkg.helper.helper import *

try:
    from pkg.helper import gv
    from pkg.helper.init import *
    from pkg.book import book
    from testing.test import test
except ImportError:
    log_error("ImportError : main.py")


def __main():
    init()
    log_info("Starting .....")
    b=book.Book()
    
    b.bookPrint()
    deinit()



def main():
    __main()


#main function starts here
main()
        




