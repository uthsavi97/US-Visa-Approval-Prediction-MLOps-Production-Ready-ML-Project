from us_Visa.logger import logging
from us_Visa.exception import USvisaException
import sys


#logging.info("welcome to our custom log")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e,sys)


