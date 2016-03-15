import logging
import datetime

logger = None

def getlogger(logfile = None,msg="initialize logger"):
    global logger
    if logger == None:
        logger = logging.getLogger()
        if logfile == None: 
            logfile = 'log/'+datetime.datetime.now().strftime("%Y%m%d") + ".log"
        else:
            logfile = 'log/'+datetime.datetime.now().strftime("%Y%m%d") + ".log"
        
        hdlr = logging.FileHandler(logfile)
        formatter = logging.Formatter('[%(lineno)d]:[%(asctime)s %(module)s] : %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        hdlr.setLevel(logging.DEBUG)
        logger.addHandler(hdlr)
        
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        ch.setLevel(logging.DEBUG)
        logger.addHandler(ch)
        
        logger.setLevel(logging.NOTSET)
       
        logger.info(msg)
    
    return logger
