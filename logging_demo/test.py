from logging_demo.setting import PROJECT_ROOT
import logging
print(PROJECT_ROOT)

from logging_demo.setting import logger

for i in range(1000):
    try:
        # open('afasdf', 'r')
        raise TypeError
    except Exception as e:
        # logger.exception(e)
        logger.exception(e)
print('done')