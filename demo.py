from us_visa.logger import logging
from us_visa.exception import USvisaException
logging.info('welcome to custom log')

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e)