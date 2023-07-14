import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path ='C:\\Nithesh\\OpenCartAutomation\\logs\\automation.log'
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    

    
    
    
    
    
    
    