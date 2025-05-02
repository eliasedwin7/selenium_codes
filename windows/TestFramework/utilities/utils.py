import logging
import inspect

class Utils :

    def assertListItmesTxt(self,value_list,value):
        for value in value_list:
            assert value.text == value 


    def cust_logger( log_level=logging.DEBUG):
        logger_name = inspect.stack()[1].function
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # Avoid adding multiple handlers if already set
        if not logger.handlers:
            # File Handler
            file_handler = logging.FileHandler('app.log')
            file_handler.setLevel(logging.DEBUG)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)

            # Formatter
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add Handlers
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
