import logging



def log_info(msg):
    print("info : " + str(msg))
    logging.info(str(msg))

def log_warn(msg):
    print("warning : " + str(msg))
    logging.warning(str(msg))

def log_error(msg):
    print("error : " + str(msg))
    logging.error(str(msg))

def log_exception(msg):
    print("exception : " + str(msg))
    logging.error(str(msg))

def log_test(msg):
    print("test : " + str(msg))
    logging.debug(str(msg))


__all__ = ['log_info', 'log_warn', 'log_error', 'log_exception', 'log_test']
